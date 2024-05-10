import os
import argparse
import json

import tiktoken

import llm
import code_utils


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process files in a folder recursively.")
    parser.add_argument("--assignment-folder", required=True, help="Path to the assignment folder.")
    parser.add_argument("--output-folder", required=True, help="Path to the output folder.")
    parser.add_argument("--model", help="Model to use for the LLM.", default="gpt-4-turbo-preview")
    parser.add_argument("--prompt-file", required=True, help="Path to the prompt file.")
    # Ablation arguments
    parser.add_argument("--exclude-non-pdf", action="store_true", help="Exclude non-PDF files from the input.")
    args = parser.parse_args()

    assignment_input_folder = os.path.join(args.assignment_folder, "input")

    file_dict = code_utils.process_files(assignment_input_folder)

    # Ablation: exclude non-PDF files from the input
    model_file_dict = {}
    if args.exclude_non_pdf:
        for filename, content in file_dict.items():
            if filename.endswith(".pdf"):
                model_file_dict[filename] = content
    else:
        model_file_dict = file_dict

    result_string = code_utils.file_dict_to_str(model_file_dict)

    enc = tiktoken.encoding_for_model("gpt-4")
    num_tokens = len(enc.encode(result_string))
    if num_tokens > code_utils.MAX_INPUT_TOKENS:
        raise ValueError(f"Input tokens ({num_tokens}) exceed the maximum limit ({code_utils.MAX_INPUT_TOKENS}).")

    # format messages
    with open(args.prompt_file, "r") as f:
        prompt = f.read()

    prompt = code_utils.replace_placeholders(prompt, {"assignment": result_string})

    messages = [
        {"role": "system", "content": "You are an expert in the field of computer science and competent programmer."},
        {"role": "user", "content": prompt},
    ]

    response = llm.call(messages, model=args.model, max_tokens=4096, temperature=0.7)

    generated_files = code_utils.extract_files(response)
    for i, (filename, code_content, is_provided) in enumerate(generated_files):
        if is_provided:
            if filename in file_dict:
                generated_files[i] = (filename, file_dict[filename], is_provided)
            else:
                raise ValueError(f"File {filename} not found in the original files.")

    # Copy over non-generated files
    for filename, content in file_dict.items():
        if filename not in [f[0] for f in generated_files]:
            generated_files.append((filename, content, True))

    # Add test files from the input folder to generated_files
    input_tests_folder = os.path.join(args.assignment_folder, "tests")
    if os.path.exists(input_tests_folder):
        for root, _, files in os.walk(input_tests_folder):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r") as f:
                        test_file_content = f.read()
                    generated_files.append((file, test_file_content, True))
    else:
        print(f"No tests folder found in the input folder: {input_tests_folder}")

    # save all files to the output folder
    model_output_folder = os.path.join(args.output_folder, "output")
    code_utils.save_files(generated_files, model_output_folder)

    # Run the unit tests
    test_results = code_utils.run_tests(generated_files)

    test_results_json_path = os.path.join(args.output_folder, "test_results.json")
    with open(test_results_json_path, "w") as f:
        json.dump(test_results, f, indent=4)

