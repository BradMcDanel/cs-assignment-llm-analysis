import os
import io
import tempfile
import unittest
import shutil

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


def save_files_to_tmp(files):
    tmp_dir = tempfile.mkdtemp(prefix='code_')
    for filename, code_content, _ in files:
        file_path = os.path.join(tmp_dir, filename)
        with open(file_path, 'w') as file:
            file.write(code_content)
    return tmp_dir

def run_tests(files, cleanup=True):
    # Save files to a temporary directory
    tmp_dir = save_files_to_tmp(files)
    
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
