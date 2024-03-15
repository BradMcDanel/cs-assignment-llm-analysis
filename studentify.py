import argparse
import os

import tiktoken

import llm
import code_utils


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process files in a folder recursively.")
    parser.add_argument("--input-folder", required=True, help="Path to the input folder with existing code.")
    parser.add_argument("--output-folder", required=True, help="Path to the output folder for studentify code.")
    parser.add_argument("--modify-files", required=True, nargs="+", help="List of file names to modify.")
    parser.add_argument("--model", help="Model to use for the LLM.", default="gpt-4-turbo-preview")
    args = parser.parse_args()

    file_dict = code_utils.process_files(args.input_folder)
    result_string = code_utils.file_dict_to_str(file_dict)

    enc = tiktoken.encoding_for_model("gpt-4")
    num_tokens = len(enc.encode(result_string))
    if num_tokens > code_utils.MAX_INPUT_TOKENS:
        raise ValueError(f"Input tokens ({num_tokens}) exceed the maximum limit ({code_utils.MAX_INPUT_TOKENS}).")

    # format messages
    with open("prompts/studentify.txt", "r") as f:
        studentify_prompt = f.read()

    modify_file_str = ", ".join(args.modify_files)

    studentify = code_utils.replace_placeholders(
        studentify_prompt, 
        {
            "assignment": result_string,
            "modify_files": modify_file_str
        }
    )

    messages = [
        {"role": "system", "content": "You are a student and this is your first ever programming assignment!"},
        {"role": "user", "content": studentify},
    ]

    # call LLM
    response = llm.call(messages, model="gpt-4-turbo-preview", max_tokens=4096, temperature=0.7)
    messages.append({"role": "assistant", "content": response})

    print(response)
    generated_files = code_utils.extract_files(response)
    for filename, code_content, is_provided in generated_files:
        # code_content = code_utils.remove_comments(code_content)
        file_dict[filename] = code_content

    # write files to output folder
    os.makedirs(args.output_folder, exist_ok=True)

    for filename, file_string in file_dict.items():
        file_path = os.path.join(args.output_folder, filename)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            f.write(file_string)

