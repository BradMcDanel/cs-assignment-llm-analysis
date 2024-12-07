import csv
import sys

def read_csv_file(filename):
    data = []
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(row)
    return data

def read_text_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def compute_longest_run(dna_sequence, str_sequence):
    longest_run = 0
    current_run = 0
    str_len = len(str_sequence)
    
    for i in range(len(dna_sequence)):
        if dna_sequence[i:i+str_len] == str_sequence:
            current_run += 1
            longest_run = max(longest_run, current_run)
        else:
            current_run = 0

    return longest_run

def identify_dna_owner(csv_data, dna_sequence):
    header = csv_data[0]
    individuals = csv_data[1:]

    for individual in individuals:
        name = individual[0]
        str_counts = individual[1:]
        match = True

        for i in range(len(str_counts)):
            str_sequence = header[i+1]
            longest_run = compute_longest_run(dna_sequence, str_sequence)
            if int(str_counts[i]) != longest_run:
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
    dna_sequence = read_text_file(dna_filename)

    owner = identify_dna_owner(csv_data, dna_sequence)
    print(owner)