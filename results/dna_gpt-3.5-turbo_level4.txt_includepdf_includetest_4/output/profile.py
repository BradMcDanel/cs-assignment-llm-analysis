import csv
import sys

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            data.append(row)
    return headers, data

def read_dna_sequence(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def compute_str_counts(headers, dna_sequence):
    str_counts = {}
    for idx, str_name in enumerate(headers[1:]):
        longest_run = 0
        current_run = 0
        str_len = len(str_name)
        for i in range(len(dna_sequence)):
            if dna_sequence[i:i+str_len] == str_name:
                current_run += 1
                longest_run = max(longest_run, current_run)
            else:
                current_run = 0
        str_counts[str_name] = longest_run
    return str_counts

def identify_dna_owner(csv_file, dna_file):
    headers, data = read_csv_file(csv_file)
    dna_sequence = read_dna_sequence(dna_file)
    str_counts = compute_str_counts(headers, dna_sequence)
    
    for row in data:
        if all(int(row[i+1]) == count for i, count in enumerate(str_counts.values())):
            print(row[0])
            return
    
    print("No match")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
    else:
        identify_dna_owner(sys.argv[1], sys.argv[2])