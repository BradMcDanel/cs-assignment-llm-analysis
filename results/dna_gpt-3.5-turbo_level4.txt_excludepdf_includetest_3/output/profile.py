import csv
import sys

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def read_dna_sequence(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def compute_longest_run(dna_sequence, str_sequence):
    longest_run = 0
    current_run = 0
    str_len = len(str_sequence)

    for i in range(len(dna_sequence)):
        if dna_sequence[i:i+str_len] == str_sequence:
            current_run += 1
            if current_run > longest_run:
                longest_run = current_run
        else:
            current_run = 0

    return longest_run

def identify_dna_owner(csv_file_path, dna_file_path):
    csv_data = read_csv_file(csv_file_path)
    dna_sequence = read_dna_sequence(dna_file_path)

    str_sequences = csv_data[0][1:]

    for row in csv_data[1:]:
        owner = row[0]
        str_counts = [int(count) for count in row[1:]]

        match = True
        for i, str_sequence in enumerate(str_sequences):
            longest_run = compute_longest_run(dna_sequence, str_sequence)
            if longest_run != str_counts[i]:
                match = False
                break

        if match:
            print(owner)
            return

    print("No match")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
    else:
        csv_file_path = sys.argv[1]
        dna_file_path = sys.argv[2]
        identify_dna_owner(csv_file_path, dna_file_path)