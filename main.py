import os
import argparse

import tiktoken

import llm
import code_utils


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process files in a folder recursively.")
    parser.add_argument("--assignment-folder", required=True, help="Path to the assignment folder.")
    parser.add_argument("--output-folder", required=True, help="Path to the output folder.")
    parser.add_argument("--model", help="Model to use for the LLM.", default="gpt-4-turbo-preview")
    args = parser.parse_args()

    file_dict = code_utils.process_files(args.assignment_folder)
    result_string = code_utils.file_dict_to_str(file_dict)

    enc = tiktoken.encoding_for_model("gpt-4")
    num_tokens = len(enc.encode(result_string))
    if num_tokens > code_utils.MAX_INPUT_TOKENS:
        raise ValueError(f"Input tokens ({num_tokens}) exceed the maximum limit ({code_utils.MAX_INPUT_TOKENS}).")

    # format messages
    with open("prompts/initial.txt", "r") as f:
        initial_prompt = f.read()

    initial = code_utils.replace_placeholders(initial_prompt, {"assignment": result_string})
    messages = [
        {"role": "system", "content": "You are an expert in the field of computer science and competent programmer."},
        {"role": "user", "content": initial},
    ]

    # call LLM
    for attempt in range(code_utils.MAX_PASS_ATTEMPTS):
        response = llm.call(messages, model="gpt-4-turbo-preview", max_tokens=4096, temperature=0.7)
        print(response)

        generated_files = code_utils.extract_files(response)

        for i, (filename, code_content, is_provided) in enumerate(generated_files):
            print(f"Generated {filename}, provided: {is_provided}")
            if is_provided:
                if filename in file_dict:
                    generated_files[i] = (filename, file_dict[filename], is_provided)
                else:
                    raise ValueError(f"File {filename} not found in the original files.")

        for filename, content in file_dict.items():
            if filename not in [f[0] for f in generated_files]:
                generated_files.append((filename, content, True))

        all_passed, test_results = code_utils.run_tests(generated_files, cleanup=False)

        if all_passed:
            break
        else:
            print(f"Attempt {attempt+1} failed")
            print(test_results)


    if not all_passed:
        print("All attempts failed")
    else:
        code_utils.save_files(generated_files, args.output_folder)

