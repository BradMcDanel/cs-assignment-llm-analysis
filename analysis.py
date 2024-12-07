import os
import json
import re

def extract_test_summary(file_path):
    empty_result = {
        "passed": 0,
        "failed": 0,
        "total": 0,
        "pass_rate": 0.0
    }
    if not os.path.exists(file_path):
        return empty_result

    with open(file_path, "r") as f:
        data = json.load(f)

    if not data:
        return empty_result
    
    summary = data.get("summary", {})
    total = summary.get("total", 0)
    collected = summary.get("collected", 0)
    passed = 0
    failed = 0

    if collected > 0 and total == 0:
        failed = collected
    else:
        passed = summary.get("passed", 0)
        failed = total - passed

    if total > 0:
        pass_rate = (passed / total) * 100
    else:
        pass_rate = 0

    return {
        "passed": passed,
        "failed": failed,
        "total": total,
        "pass_rate": pass_rate
    }

def parse_filename(filename):
    pattern = r'^(.+?)_(.+?)_(.+?)_(includepdf|includetest|excludepdf|excludetest)_(includepdf|includetest|excludepdf|excludetest)_(\d+)$'
    match = re.match(pattern, filename)
    if match:
        input_dir, model, prompt_file, pdf_setting, test_setting, iteration = match.groups()
        return {
            'input_dir': input_dir,
            'model': model,
            'prompt_file': prompt_file,
            'include_pdf': pdf_setting in ['includepdf'],
            'include_test': test_setting in ['includetest'],
            'iteration': int(iteration)
        }
    return None

def read_test_results(directory):
    test_results_path = os.path.join(directory, 'test_results.json')
    return extract_test_summary(test_results_path)

def analyze_results(base_output_dir):
    results = []
    
    for folder_name in os.listdir(base_output_dir):
        folder_path = os.path.join(base_output_dir, folder_name)
        if os.path.isdir(folder_path):
            settings = parse_filename(folder_name)
            if settings:
                summary = read_test_results(folder_path)
                if summary:
                    results.append((settings, summary))
    
    return results

def main():
    base_output_dir = "results"
    individual_results = analyze_results(base_output_dir)

    print("Individual Results:\n")
    for settings, summary in individual_results:
        print(f"Settings:")
        print(f"  Input Directory: {settings['input_dir']}")
        print(f"  Model: {settings['model']}")
        print(f"  Prompt File: {settings['prompt_file']}")
        print(f"  Include PDF: {settings['include_pdf']}")
        print(f"  Include Test: {settings['include_test']}")
        print(f"  Iteration: {settings['iteration']}")
        print(f"Summary:")
        print(f"  Passed: {summary['passed']}")
        print(f"  Failed: {summary['failed']}")
        print(f"  Total: {summary['total']}")
        print(f"  Pass Rate: {summary['pass_rate']:.2f}%")
        print()

if __name__ == "__main__":
    main()
