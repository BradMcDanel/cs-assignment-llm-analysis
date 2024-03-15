import os
import io
import tempfile
import unittest
import shutil

def extract_files(document_content):
    sections = document_content.split('```')
    files = []
    for section in sections:
        if section.strip().startswith('python\n###'):
            # Process the section
            header_and_code = section.split('\n', 1)[1]  # Skip the 'python' line
            header, code = header_and_code.split('\n', 1)
            header = header.strip('#').strip()  # Remove leading and trailing # and spaces
            filename = ''
            is_provided = False

            # Parse the header for filename and provided status
            if '- PROVIDED' in header:
                filename, _ = header.split('- PROVIDED')
                is_provided = True
            else:
                filename = header

            filename = filename.strip()
            # Search for .py in the parsed filename or any part if it's in a longer string
            if '.py' not in filename:
                parts = filename.split()
                for part in parts:
                    if '.py' in part:
                        filename = part
                        break

            # Clean up code content, ensuring it does not start with a newline
            code_content = code.strip()

            files.append((filename, code_content, is_provided))

    return files


def save_files_to_tmp(files):
    tmp_dir = tempfile.mkdtemp(prefix='code_')
    for filename, code_content, _ in files:
        file_path = os.path.join(tmp_dir, filename)
        with open(file_path, 'w') as file:
            file.write(code_content)
    return tmp_dir

def run_tests(files, cleanup=True):
    tmp_dir = save_files_to_tmp(files)
    test_suite = unittest.TestLoader().discover(tmp_dir, pattern='test_*.py')
    
    # Create a StringIO object to capture the test output
    test_output = io.StringIO()
    
    # Create a TextTestRunner with the StringIO object as the stream
    test_runner = unittest.TextTestRunner(stream=test_output)
    
    # Run the tests
    test_result = test_runner.run(test_suite)
    
    # Get the captured output as a string
    test_results = test_output.getvalue()
    
    # Close the StringIO object
    test_output.close()
    
    # Check if all tests passed
    all_tests_passed = test_result.wasSuccessful()
    
    # Clean up the temporary directory if the cleanup flag is True
    if cleanup:
        shutil.rmtree(tmp_dir)
    
    return all_tests_passed, test_results


if __name__=="__main__":
    with open("response.txt", "r") as file:
        response = file.read()

    generated_files = extract_files(response) 

    for filename, code_content, is_provided in generated_files:
        print(f"Generated {filename}, provided: {is_provided}")
        print(code_content)
