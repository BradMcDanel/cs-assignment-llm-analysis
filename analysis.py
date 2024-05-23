import os
import json
import re
from collections import defaultdict

def extract_test_summary(file_path):
    if not os.path.exists(file_path):
        return {
            "passed": 0,
            "failed": 1,
            "total": 1,
            "pass_rate": 0.0
        }

    with open(file_path, "r") as f:
        data = json.load(f)
    
    summary = data.get("summary", {})
    passed = summary.get("passed", 0)
    failed = summary.get("failed", 0)
    total = summary.get("total", 0)
    
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
    pattern = r'^(.*?)_(.*?)_(.*?)_(excludepdf|includepdf)_(\d+)$'
    match = re.match(pattern, filename)
    if match:
        input_dir, model, prompt_file, exclude_pdf, iteration = match.groups()
        return {
            'input_dir': input_dir,
            'model': model,
            'prompt_file': prompt_file,
            'exclude_pdf': exclude_pdf == 'excludepdf',
            'iteration': int(iteration)
        }
    return None

def read_test_results(directory):
    test_results_path = os.path.join(directory, 'test_results.json')
    if os.path.exists(test_results_path):
        return extract_test_summary(test_results_path)
    return None

def analyze_results(base_output_dir):
    results = []
    aggregated_results = defaultdict(lambda: {'passed': 0, 'failed': 0, 'total': 0, 'pass_rate': 0, 'count': 0})
    
    for folder_name in os.listdir(base_output_dir):
        folder_path = os.path.join(base_output_dir, folder_name)
        if os.path.isdir(folder_path):
            settings = parse_filename(folder_name)
            if settings:
                summary = read_test_results(folder_path)
                if summary:
                    results.append((settings, summary))
                    
                    key = (settings['input_dir'], settings['model'], settings['prompt_file'], settings['exclude_pdf'])
                    aggregated_results[key]['passed'] += summary['passed']
                    aggregated_results[key]['failed'] += summary['failed']
                    aggregated_results[key]['total'] += summary['total']
                    aggregated_results[key]['pass_rate'] += summary['pass_rate']
                    aggregated_results[key]['count'] += 1

    # Print individual results
    for settings, summary in results:
        print(f"Settings: {settings}")
        print(f"Summary: {summary}\n")
    
    # Calculate and print aggregated results
    print("Aggregated Results:\n")
    for key, agg in aggregated_results.items():
        agg_summary = {
            "passed": agg["passed"] / agg["count"],
            "failed": agg["failed"] / agg["count"],
            "total": agg["total"] / agg["count"],
            "pass_rate": agg["pass_rate"] / agg["count"]
        }
        input_dir, model, prompt_file, exclude_pdf = key
        print(f"Settings: input_dir={input_dir}, model={model}, prompt_file={prompt_file}, exclude_non_pdf={exclude_pdf}")
        print(f"Summary: {agg_summary}\n")

if __name__ == "__main__":
    base_output_dir = "results"  # Adjust this as necessary
    analyze_results(base_output_dir)

