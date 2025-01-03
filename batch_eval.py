import os
import argparse
from itertools import product
from process_assignment import process_assignment
from tqdm import tqdm
import time
import json

def get_completed_runs(output_dir):
    """Track completed runs using a metadata file"""
    metadata_file = os.path.join(output_dir, "evaluation_metadata.json")
    if os.path.exists(metadata_file):
        with open(metadata_file, 'r') as f:
            return json.load(f)
    return {}

def save_run_metadata(output_dir, run_info):
    """Save metadata about completed runs"""
    metadata_file = os.path.join(output_dir, "evaluation_metadata.json")
    with open(metadata_file, 'w') as f:
        json.dump(run_info, f, indent=2)

def batch_evaluate(settings):
    combinations = list(product(
        settings['input_dirs'],
        settings['models'],
        settings['prompt_files'],
        settings['exclude_non_pdf'],
        settings['exclude_tests'],
        range(settings['num_evaluations'])
    ))
    
    # Create base output directory if it doesn't exist
    os.makedirs(settings['base_output_dir'], exist_ok=True)
    
    # Load existing run metadata
    completed_runs = get_completed_runs(settings['base_output_dir'])
    
    total_combinations = len(combinations)
    with tqdm(total=total_combinations, disable=settings['silent'], ncols=100, desc="Processing assignments") as pbar:
        for input_dir, model, prompt_file, exclude_non_pdf, exclude_tests, iteration in combinations:
            exclude_pdf_flag = 'exclude' if exclude_non_pdf else 'include'
            exclude_tests_flag = 'exclude' if exclude_tests else 'include'
            output_dir_name = f"{os.path.basename(input_dir)}_{model}_{os.path.basename(prompt_file)}_{exclude_pdf_flag}pdf_{exclude_tests_flag}test_{iteration}"
            output_dir = os.path.join(settings['base_output_dir'], output_dir_name)
            
            # Check if this combination has been successfully completed
            run_key = f"{output_dir_name}"
            if run_key in completed_runs and not settings.get('force_reprocess', False):
                pbar.write(f"Skipping previously completed run: {output_dir}")
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
                    exclude_non_pdf=exclude_non_pdf,
                    exclude_tests=exclude_tests
                )
                
                # Record successful completion
                completed_runs[run_key] = {
                    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                    'elapsed_time': time.time() - start_time,
                    'parameters': {
                        'input_dir': input_dir,
                        'model': model,
                        'prompt_file': prompt_file,
                        'exclude_non_pdf': exclude_non_pdf,
                        'exclude_tests': exclude_tests,
                        'iteration': iteration
                    }
                }
                save_run_metadata(settings['base_output_dir'], completed_runs)
                
            except Exception as e:
                pbar.write(f"Error processing assignment: {e}")
                # Optionally save error information
                completed_runs[run_key] = {
                    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                    'error': str(e),
                    'parameters': {
                        'input_dir': input_dir,
                        'model': model,
                        'prompt_file': prompt_file,
                        'exclude_non_pdf': exclude_non_pdf,
                        'exclude_tests': exclude_tests,
                        'iteration': iteration
                    }
                }
                save_run_metadata(settings['base_output_dir'], completed_runs)
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
    parser.add_argument("--exclude-tests", nargs="+", type=str, required=True, help="List of boolean values to exclude test files from the input.")
    parser.add_argument("--input-dirs", nargs='+', required=True, help="List of input directories.")
    parser.add_argument("--base-output-dir", required=True, help="Base path for the output directories.")
    parser.add_argument("--silent", action="store_true", help="Suppress progress output.")
    parser.add_argument("--force-reprocess", action="store_true", help="Force reprocessing of existing outputs.")
    
    args = parser.parse_args()
    args.exclude_non_pdf = [True if x.lower() == 'true' else False for x in args.exclude_non_pdf]
    args.exclude_tests = [True if x.lower() == 'true' else False for x in args.exclude_tests]
    
    settings = vars(args)
    batch_evaluate(settings)
