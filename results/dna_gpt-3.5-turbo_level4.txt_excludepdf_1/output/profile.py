import csv
import sys

def read_csv_file(file_name):
    data = []
    with open(file_name, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(row)
    return data

def read_dna_sequence(file_name):
    with open(file_name, 'r') as file:
        dna_sequence = file.read().replace('\n', '')
    return dna_sequence

def compute_longest_run(dna_sequence, str_sequence):
    longest_run = 0
    current_run = 0
    str_length = len(str_sequence)
    
    for i in range(len(dna_sequence)):
        if dna_sequence[i:i+str_length] == str_sequence:
            current_run += 1
            if current_run > longest_run:
                longest_run = current_run
        else:
            current_run = 0

    return longest_run

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    csv_file = sys.argv[1]
    dna_file = sys.argv[2]

    data = read_csv_file(csv_file)
    dna_sequence = read_dna_sequence(dna_file)

    # Get the STR sequences from the CSV file
    str_sequences = data[0][1:]

    # Compute the longest run of each STR in the DNA sequence
    longest_runs = {str_sequence: compute_longest_run(dna_sequence, str_sequence) for str_sequence in str_sequences}

    # Compare the computed longest runs with the individuals in the CSV file
    for row in data[1:]:
        name = row[0]
        str_counts = list(map(int, row[1:]))
        if all(str_counts[str_sequences.index(str_sequence)] == longest_runs[str_sequence] for str_sequence in str_sequences):
            print(name)
            sys.exit(0)
    
    print("No match")

if __name__ == "__main__":
    main()