import os
import argparse
from itertools import product
from process_assignment import process_assignment
from tqdm import tqdm
import time

def batch_evaluate(settings):
    combinations = list(product(
        settings['input_dirs'],
        settings['models'],
        settings['prompt_files'],
        settings['exclude_non_pdf'],
        range(settings['num_evaluations'])
    ))

    total_combinations = len(combinations)

    with tqdm(total=total_combinations, disable=settings['silent'], ncols=100, desc="Processing assignments") as pbar:
        for input_dir, model, prompt_file, exclude_non_pdf, iteration in combinations:
            exclude_flag = 'exclude' if exclude_non_pdf else 'include'
            output_dir_name = f"{os.path.basename(input_dir)}_{model}_{os.path.basename(prompt_file)}_{exclude_flag}pdf_{iteration}"
            output_dir = os.path.join(settings['base_output_dir'], output_dir_name)

            if os.path.exists(output_dir):
                pbar.write(f"Skipping existing output directory: {output_dir}")
                pbar.update(1)
                continue

            os.makedirs(output_dir, exist_ok=True)

            start_time = time.time()
            try:
                process_assignment(
                    assignment_folder=input_dir,
                    output_folder=output_dir,
                    prompt_file=prompt_file,
                    model=model,
                    exclude_non_pdf=exclude_non_pdf
                )
            except Exception as e:
                pbar.write(f"Error processing assignment: {e}")
                pbar.update(1)
                continue
            elapsed_time = time.time() - start_time

            pbar.set_postfix_str(f"Last task took: {elapsed_time:.2f}s")
            pbar.update(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch evaluate multiple input directories with different models and prompts.")
    parser.add_argument("--num-evaluations", type=int, required=True, help="Number of evaluations per input.")
    parser.add_argument("--models", nargs='+', required=True, help="List of models to use for the LLM.")
    parser.add_argument("--prompt-files", nargs='+', required=True, help="List of paths to the prompt files.")
    parser.add_argument("--exclude-non-pdf", nargs='+', type=str, required=True, help="List of boolean values to exclude non-PDF files from the input.")
    parser.add_argument("--input-dirs", nargs='+', required=True, help="List of input directories.")
    parser.add_argument("--base-output-dir", required=True, help="Base path for the output directories.")
    parser.add_argument("--silent", action="store_true", help="Suppress progress output.")
    
    args = parser.parse_args()
    args.exclude_non_pdf = [True if x.lower() == 'true' else False for x in args.exclude_non_pdf]

    settings = {
        'num_evaluations': args.num_evaluations,
        'models': args.models,
        'prompt_files': args.prompt_files,
        'exclude_non_pdf': args.exclude_non_pdf,
        'input_dirs': args.input_dirs,
        'base_output_dir': args.base_output_dir,
        'silent': args.silent
    }

    batch_evaluate(settings)

