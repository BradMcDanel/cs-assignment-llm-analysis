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
        text += pytesseract.image_to_string(image)

    return text

FILE_TYPES = [
    (".pdf", process_pdf),
    (".txt", lambda path: open(path, "r").read()),
    (".py", lambda path: open(path, "r").read()),
    # Add more file types and their corresponding processing functions here
]

def process_files(folder_path):
    result = ""
    file_list = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, folder_path)
            file_list.append((file_path, relative_path))

    # Sort the files based on the order of file types in FILE_TYPES
    file_list.sort(key=lambda x: next((i for i, (ext, _) in enumerate(FILE_TYPES) if x[0].endswith(ext)), len(FILE_TYPES)))

    for file_path, relative_path in file_list:
        for ext, process_func in FILE_TYPES:
            if file_path.endswith(ext):
                result += f"\n# {relative_path}\n"
                result += process_func(file_path)
                break

    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process files in a folder recursively.")
    parser.add_argument("--assignment-folder", help="Path to the assignment folder.")
    parser.add_argument("--output-folder", help="Path to the output folder.")
    args = parser.parse_args()
    folder_path = args.assignment_folder
    result_string = process_files(args.assignment_folder)

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
    response = llm.call(messages, model="gpt-4-turbo-preview", max_tokens=4096, temperature=0.7)
    messages.append({"role": "assistant", "content": response})

    for attempt in range(MAX_PASS_ATTEMPTS):
        all_passed, test_results = code_utils.run_tests(response, cleanup=False)
        if all_passed:
            break
        else:
            print(f"Attempt {attempt+1} failed")
            print(response)
            print(test_results)

            fix = replace_placeholders(fix_prompt, {"test_results": test_results})
            messages.append({"role": "user", "content": fix})

            response = llm.call(messages, model="gpt-4-turbo-preview", max_tokens=4096, temperature=0.7)
            messages.append({"role": "assistant", "content": response})

    if not all_passed:
        print("All attempts failed")
    else:
        print(f"All tests passed - saving files to {args.output_folder}")
        files = code_utils.extract_files(response)
        os.makedirs(args.output_folder, exist_ok=True)
        for filename, code_content in files:
            with open(os.path.join(args.output_folder, filename), "w") as f:
                f.write(code_content)

