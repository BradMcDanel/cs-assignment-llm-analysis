import csv
import sys

def read_csv(file_name):
    data = []
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def read_dna_sequence(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def compute_str_counts(dna_sequence, str_sequence):
    longest_runs = []
    for str_type in str_sequence.keys():
        longest_run = 0
        current_run = 0
        str_length = len(str_type)
        for i in range(len(dna_sequence)):
            if dna_sequence[i:i+str_length] == str_type:
                current_run += 1
                i += str_length - 1
            else:
                if current_run > longest_run:
                    longest_run = current_run
                current_run = 0
        longest_runs.append(longest_run)
    return longest_runs

def identify_match(csv_data, dna_sequence):
    str_sequence = csv_data[0]
    for row in csv_data[1:]:
        str_counts = {key: int(value) for key, value in row.items()}
        longest_runs = compute_str_counts(dna_sequence, str_sequence)
        if longest_runs == list(str_counts.values()):
            return row['name']
    return "No match"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    csv_file = sys.argv[1]
    dna_file = sys.argv[2]

    csv_data = read_csv(csv_file)
    dna_sequence = read_dna_sequence(dna_file)

    match = identify_match(csv_data, dna_sequence)
    print(match)