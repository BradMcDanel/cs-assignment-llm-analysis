import csv
import sys

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def read_dna_sequence(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def identify_dna_owner(csv_data, dna_sequence):
    header = csv_data[0]
    str_counts = {header[i]: 0 for i in range(1, len(header))}
    for i in range(1, len(header)):
        str_counts[header[i]] = get_longest_run(header[i], dna_sequence)

    for row in csv_data[1:]:
        match = True
        for i in range(1, len(row)):
            if int(row[i]) != str_counts[header[i]]:
                match = False
                break
        if match:
            return row[0]

    return "No match"

def get_longest_run(str_sequence, dna_sequence):
    longest_run = 0
    current_run = 0
    str_len = len(str_sequence)

    i = 0
    while i < len(dna_sequence) - str_len:
        if dna_sequence[i:i+str_len] == str_sequence:
            current_run += 1
            i += str_len
        else:
            current_run = 0
            i += 1

        if current_run > longest_run:
            longest_run = current_run

    return longest_run

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
    else:
        csv_file_path = sys.argv[1]
        dna_file_path = sys.argv[2]

        csv_data = read_csv_file(csv_file_path)
        dna_sequence = read_dna_sequence(dna_file_path)

        owner = identify_dna_owner(csv_data, dna_sequence)
        print(owner)