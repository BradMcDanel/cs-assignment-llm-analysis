import csv
import sys

def read_csv_file(filename):
    data = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data[row['name']] = {k: int(v) for k, v in row.items() if k != 'name'}
    return data

def read_dna_sequence(filename):
    with open(filename, 'r') as file:
        return file.read()

def compute_longest_run(dna_sequence, str_sequence):
    longest_run = 0
    current_run = 0
    str_length = len(str_sequence)

    for i in range(len(dna_sequence)):
        if dna_sequence[i:i+str_length] == str_sequence:
            current_run += 1
            longest_run = max(longest_run, current_run)
        else:
            current_run = 0

    return longest_run

def identify_dna_owner(csv_data, dna_sequence):
    for name, str_counts in csv_data.items():
        match = True
        for str_name, str_count in str_counts.items():
            longest_run = compute_longest_run(dna_sequence, str_name)
            if longest_run != str_count:
                match = False
                break
        if match:
            return name

    return "No match"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    csv_filename = sys.argv[1]
    dna_filename = sys.argv[2]

    csv_data = read_csv_file(csv_filename)
    dna_sequence = read_dna_sequence(dna_filename)

    result = identify_dna_owner(csv_data, dna_sequence)
    print(result)