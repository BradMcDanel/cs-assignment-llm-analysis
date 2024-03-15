import os
import io
import tempfile
import unittest
import re
import shutil


def extract_files(document_content):
    pattern = r'```python\n# (.*?)\n(.*?)```'
    matches = re.findall(pattern, document_content, re.DOTALL)
    files = [(filename, code_content.strip()) for filename, code_content in matches]
    return files

def save_files_to_tmp(files):
    tmp_dir = tempfile.mkdtemp(prefix='code_')
    for filename, code_content in files:
        file_path = os.path.join(tmp_dir, filename)
        with open(file_path, 'w') as file:
            file.write(code_content)
    return tmp_dir

def run_tests(response, cleanup=True):
    files = extract_files(response)
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

    all_passed, test_results = run_tests(response)
    print(all_passed)
    if not all_passed:
        print(test_results)
