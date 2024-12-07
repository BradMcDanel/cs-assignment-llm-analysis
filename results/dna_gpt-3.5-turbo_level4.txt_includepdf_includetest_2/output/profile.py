import csv
import sys

def read_csv(file_path):
    data = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data[row['name']] = {k: int(v) for k, v in row.items() if k != 'name'}
    return data

def read_sequence(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def compute_str_counts(dna_sequence, str_counts):
    longest_runs = {name: 0 for name in str_counts}
    for name, counts in str_counts.items():
        for str_name, str_count in counts.items():
            cur_count = 0
            for i in range(len(dna_sequence)):
                if dna_sequence[i:i+len(str_name)] == str_name:
                    cur_count += 1
                else:
                    longest_runs[name] = max(longest_runs[name], cur_count)
                    cur_count = 0
        longest_runs[name] = max(longest_runs[name], cur_count)
    return longest_runs

def identify_dna_owner(csv_file, sequence_file):
    str_counts = read_csv(csv_file)
    dna_sequence = read_sequence(sequence_file)
    longest_runs = compute_str_counts(dna_sequence, str_counts)
    
    for name, counts in str_counts.items():
        if counts == longest_runs:
            return name

    return "No match"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py <csv_file> <sequence_file>")
        sys.exit(1)

    csv_file = sys.argv[1]
    sequence_file = sys.argv[2]
    result = identify_dna_owner(csv_file, sequence_file)
    print(result)