import os
import argparse
import re

import pytesseract
from pdf2image import convert_from_path
import tiktoken

import llm
import code_utils

MAX_INPUT_TOKENS = 8192
MAX_PASS_ATTEMPTS = 1

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
    for i, (relative_path, file_string) in enumerate(file_dict.items()):
        ext = os.path.splitext(relative_path)[1]
        result += f"# {relative_path}\n"
        postprocess_func = FILE_TYPES[ext]["postprocess_func"]
        result += postprocess_func(file_string)
        if i < len(file_dict) - 1:
            result += "\n"
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process files in a folder recursively.")
    parser.add_argument("--assignment-folder", help="Path to the assignment folder.")
    parser.add_argument("--output-folder", help="Path to the output folder.")
    parser.add_argument("--model", help="Model to use for the LLM.", default="gpt-4-turbo-preview")
    args = parser.parse_args()

    file_dict = process_files(args.assignment_folder)
    result_string = file_dict_to_str(file_dict)

    enc = tiktoken.encoding_for_model("gpt-4")
    num_tokens = len(enc.encode(result_string))
    if num_tokens > MAX_INPUT_TOKENS:
        raise ValueError(f"Input tokens ({num_tokens}) exceed the maximum limit ({MAX_INPUT_TOKENS}).")

    # format messages
    with open("prompts/initial.txt", "r") as f:
        initial_prompt = f.read()

    with open("prompts/fix.txt", "r") as f:
        fix_prompt = f.read()

    initial = replace_placeholders(initial_prompt, {"assignment": result_string})
    messages = [
        {"role": "system", "content": "You are an expert in the field of computer science and competent programmer."},
        {"role": "user", "content": initial},
    ]

    # call LLM
    for attempt in range(MAX_PASS_ATTEMPTS):
        response = llm.call(messages, model="gpt-4-turbo-preview", max_tokens=4096, temperature=0.7)
        messages.append({"role": "assistant", "content": response})
        print(response)

        generated_files = code_utils.extract_files(response)

        for i, (filename, code_content, is_provided) in enumerate(generated_files):
            print(f"Generated {filename}, provided: {is_provided}")
            if is_provided:
                if filename in file_dict:
                    generated_files[i] = (filename, file_dict[filename], is_provided)
                else:
                    raise ValueError(f"File {filename} not found in the original files.")

        # also copy over all .txt and .csv files that were not generated
        for filename, file_string in file_dict.items():
            if filename not in [f[0] for f in generated_files]:
                ext = os.path.splitext(filename)[1]
                if ext in [".txt", ".csv"]:
                    generated_files.append((filename, file_string, True))

        all_passed, test_results = code_utils.run_tests(generated_files, cleanup=False)

        if all_passed:
            break
        else:
            print(f"Attempt {attempt+1} failed")
            print(test_results)

            fix = replace_placeholders(fix_prompt, {"test_results": test_results})
            messages.append({"role": "user", "content": fix})

    if not all_passed:
        print("All attempts failed")
    else:
        print(f"All tests passed - saving files to {args.output_folder}")
        os.makedirs(args.output_folder, exist_ok=True)
        for filename, code_content, _ in generated_files:
            with open(os.path.join(args.output_folder, filename), "w") as f:
                f.write(code_content)

