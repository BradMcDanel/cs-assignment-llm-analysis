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
    total = summary.get("total", 0)
    collected = summary.get("collected", 0)
    passed = 0
    failed = 0

    if collected > 0 and total == 0:
        # If tests were collected but not executed, consider them all as failed
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
    pattern = r'^(.*?)_(.*?)_(.*?)_(includepdf|includetest|excludepdf|excludetest)_(\d+)$'
    match = re.match(pattern, filename)
    if match:
        input_dir, model, prompt_file, include_test, iteration = match.groups()
        return {
            'input_dir': input_dir,
            'model': model,
            'prompt_file': prompt_file,
            'include_test': include_test in ['includepdf', 'includetest'],
            'iteration': int(iteration)
        }
    return None

def read_test_results(directory):
    test_results_path = os.path.join(directory, 'test_results.json')
    return extract_test_summary(test_results_path)

def repair_invalid_tests(results):
    grouped_results = defaultdict(list)
    for settings, summary in results:
        key = (settings['input_dir'], settings['model'], settings['prompt_file'], settings['include_test'])
        grouped_results[key].append((settings, summary))
    
    repaired_results = []
    
    for key, summaries in grouped_results.items():
        valid_totals = [summary['total'] for _, summary in summaries if summary['total'] > 1]
        max_tests = max(valid_totals) if valid_totals else 1
        
        for settings, summary in summaries:
            if summary['total'] == 1 and summary['failed'] == 1 and max_tests > 1:
                summary['failed'] = max_tests
                summary['total'] = max_tests
                summary['pass_rate'] = 0.0
            
            repaired_results.append((settings, summary))
    
    return repaired_results

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
    
    results = repair_invalid_tests(results)
    
    for settings, summary in results:
        key = (settings['input_dir'], settings['model'], settings['prompt_file'], settings['include_test'])
        aggregated_results[key]['passed'] += summary['passed']
        aggregated_results[key]['failed'] += summary['failed']
        aggregated_results[key]['total'] += summary['total']
        aggregated_results[key]['pass_rate'] += summary['pass_rate']
        aggregated_results[key]['count'] += 1

    aggregated_summary = {}
    for key, agg in aggregated_results.items():
        pass_rate = (agg["passed"] / agg["total"]) * 100 if agg["total"] > 0 else 0.0

        agg_summary = {
            "passed": agg["passed"] / agg["count"],
            "failed": agg["failed"] / agg["count"],
            "total": agg["total"] / agg["count"],
            "pass_rate": pass_rate,
            "num_evaluations": agg["count"]
        }
        aggregated_summary[key] = agg_summary

    return results, aggregated_summary

def main():
    base_output_dir = "results"
    individual_results, aggregated_summary = analyze_results(base_output_dir)

    print("Aggregated Results:\n")
    for key, agg_summary in aggregated_summary.items():
        input_dir, model, prompt_file, include_test = key
        print(f"Settings: input_dir={input_dir}, model={model}, prompt_file={prompt_file}, include_test={include_test}")
        print(f"Summary: {agg_summary}\n")

    print("Individual Results:\n")
    for settings, summary in individual_results:
        print(f"Settings: {settings}")
        print(f"Summary: {summary}\n")

if __name__ == "__main__":
    main()

