import csv
import sys

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def read_dna_sequence(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def compute_longest_run(dna_sequence, str_sequence):
    longest_run = 0
    current_run = 0
    str_len = len(str_sequence)

    for i in range(len(dna_sequence) - str_len):
        if dna_sequence[i:i+str_len] == str_sequence:
            current_run += 1
            longest_run = max(longest_run, current_run)
        else:
            current_run = 0

    return longest_run

def identify_dna_owner(csv_data, dna_sequence):
    headers = csv_data[0][1:]
    for row in csv_data[1:]:
        name = row[0]
        str_counts = [int(count) for count in row[1:]]
        matches = [compute_longest_run(dna_sequence, str_sequence) == count for str_sequence, count in zip(headers, str_counts)]
        if all(matches):
            return name
    
    return "No match"

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    csv_data = read_csv(sys.argv[1])
    dna_sequence = read_dna_sequence(sys.argv[2])
    owner = identify_dna_owner(csv_data, dna_sequence)
    print(owner)