import os
import io
import tempfile
import unittest
import shutil
import re

import pytesseract
from pdf2image import convert_from_path
from PIL import Image

MAX_INPUT_TOKENS = 16384
MAX_PASS_ATTEMPTS = 1

FILE_ORDER = [".pdf", ".txt", ".csv", ".py", "*"]

def remove_comments(code):
    # Remove single-line comments
    code = re.sub(r'#.*', '', code)

    # Remove multi-line comments
    code = re.sub(r'""".*?"""', '', code, flags=re.DOTALL)
    code = re.sub(r"'''.*?'''", '', code, flags=re.DOTALL)

    code = re.sub(r'^\s*\n', '', code, flags=re.MULTILINE)

    return code

def replace_placeholders(string, prompt_args):
    def replace(match):
        key = match.group(1)
        return prompt_args.get(key, match.group(0))

    return re.sub(r'<\|(.+?)\|>', replace, string)

def process_pdf(pdf_path):
    # Convert PDF to images
    images = convert_from_path(pdf_path)

    # Perform OCR on each image
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image, config="--psm 6")

    return text

def trim_collections(file_string, max_entries=50):
    # Regex pattern to match lists and dictionaries
    pattern = r'(\[.*?\]|\{.*?\})'

    def replace(match):
        content = match.group(1)
        if content.startswith('['):
            # Trim list
            items = re.findall(r'(\w+|\d+|\[.*?\]|\{.*?\}|\'.*?\'|".*?")', content)
            if len(items) > max_entries:
                trimmed_content = '[' + ', '.join(items[:max_entries//2]) + ", " + ', '.join(items[-max_entries//2:]) + ']'
                return trimmed_content
        else:
            # Trim dictionary
            items = re.findall(r'(\'.*?\': .*?)(,|\})', content)
            if len(items) > max_entries:
                trimmed_items = items[:max_entries//2] + items[-max_entries//2:]
                trimmed_content = '{' + ', '.join([item[0] for item in trimmed_items]) + '}'
                return trimmed_content
        return match.group(0)

    trimmed_file_string = re.sub(pattern, replace, file_string, flags=re.DOTALL)
    return trimmed_file_string

def postprocess_python(file_string):
    file_string = trim_collections(file_string)
    return file_string

def postprocess_csv(file_string, n=20):
    lines = file_string.split('\n')
    total_lines = len(lines)
    
    if total_lines <= 2*n:
        # If total lines are less than or equal to 2n, return the original string
        return file_string
    else:
        # Keep the first n lines and the last n lines
        trimmed_lines = lines[:n] + lines[-n:]
        return '\n'.join(trimmed_lines)

FILE_TYPES = {
    "*": {
        "process_func": lambda path: open(path, "rb").read(),
        "postprocess_func": lambda s: s,
    },
    ".pdf": {
        "process_func": process_pdf,
        "postprocess_func": lambda s: s,
    },
    ".txt": {
        "process_func": lambda path: open(path, "r").read(),
        "postprocess_func": lambda s: s,
    },
    ".csv": {
        "process_func": lambda path: open(path, "r").read(),
        "postprocess_func": postprocess_csv,
    },
    ".py": {
        "process_func": lambda path: open(path, "r").read(),
        "postprocess_func": postprocess_python,
    },
    ".png": {
        "process_func": lambda path: Image.open(path),
        "postprocess_func": lambda _: "", # don't include images in the response
    }
}

def process_files(folder_path):
    file_dict = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, folder_path)
            ext = os.path.splitext(file_path)[1]
            if ext in FILE_TYPES:
                process_func = FILE_TYPES[ext]["process_func"]
                file_dict[relative_path] = process_func(file_path)
    return file_dict

def file_dict_to_str(file_dict):
    result = ""
    remaining_files = list(file_dict.items())

    for ext in FILE_ORDER:
        for relative_path, file_string in list(remaining_files):
            if ext == "*" or os.path.splitext(relative_path)[1] == ext:
                result += f"# {relative_path}\n"
                postprocess_func = FILE_TYPES[os.path.splitext(relative_path)[1]]["postprocess_func"]
                result += postprocess_func(file_string)
                result += "\n"
                remaining_files.remove((relative_path, file_string))

    return result.rstrip("\n")

def extract_files(document_content):
    sections = document_content.split('```')
    files = []

    for section in sections:
        if section.strip().startswith('python\n###') or section.strip().startswith('plaintext\n###'):
            # Process the section
            header_and_content = section.split('\n', 1)[1]  # Skip the first line indicating language/type
            header, content = header_and_content.split('\n', 1)
            header = header.strip('#').strip()  # Remove leading and trailing # and spaces
            filename = ''
            is_provided = False

            # Determine if the file is marked as provided
            if '- PROVIDED' in header:
                filename, _ = header.split('- PROVIDED')
                is_provided = True
            else:
                filename = header

            filename = filename.strip()

            # For plaintext files without a clear .txt in the header, set a default .txt extension
            if 'plaintext\n###' in section and not filename.endswith('.txt'):
                filename += '.txt'

            # Clean up code/content, ensuring it does not start with a newline
            content = content.strip()

            files.append((filename, content, is_provided))

    return files

def save_files(files, save_dir=None):
    if save_dir is None:
        save_dir = tempfile.mkdtemp(prefix='code_')

    for filename, content, _ in files:
        file_path = os.path.join(save_dir, filename)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        print(f"Saving {filename} to {file_path}")
        if hasattr(content, "save"):
            content.save(file_path)
        else:
            with open(file_path, "w") as f:
                f.write(content)

    return save_dir

def run_tests(files, cleanup=True):
    # Save files to a temporary directory
    tmp_dir = save_files(files)
    
    # Save the current working directory
    original_cwd = os.getcwd()
    
    # Change the current working directory to the temporary directory
    os.chdir(tmp_dir)
    
    try:
        test_suite = unittest.TestLoader().discover('.', pattern='test_*.py')
        
        test_output = io.StringIO()
        test_runner = unittest.TextTestRunner(stream=test_output)
        test_result = test_runner.run(test_suite)
        
        test_results = test_output.getvalue()
    finally:
        # Close the StringIO object
        test_output.close()
        
        # Change back to the original directory
        os.chdir(original_cwd)
        
        # Clean up the temporary directory if the cleanup flag is True
        if cleanup:
            shutil.rmtree(tmp_dir)
    
    all_tests_passed = test_result.wasSuccessful()
    
    return all_tests_passed, test_results

if __name__=="__main__":
    with open("response.txt", "r") as file:
        response = file.read()

    generated_files = extract_files(response) 

    for filename, code_content, is_provided in generated_files:
        print(f"Generated {filename}, provided: {is_provided}")
        print(code_content)
