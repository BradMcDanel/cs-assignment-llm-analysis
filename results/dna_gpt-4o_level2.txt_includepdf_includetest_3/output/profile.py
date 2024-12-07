import csv
import sys

def read_csv_file(filename):
    with open(filename) as file:
        reader = csv.DictReader(file)
        dna_database = [row for row in reader]
    return dna_database

def read_dna_sequence(filename):
    with open(filename) as file:
        dna_sequence = file.read().strip()
    return dna_sequence

def longest_match(sequence, subsequence):
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    for i in range(sequence_length):
        count = 0
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        longest_run = max(longest_run, count)
    return longest_run

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python profile.py data.csv sequence.txt")

    csv_filename = sys.argv[1]
    dna_filename = sys.argv[2]

    dna_database = read_csv_file(csv_filename)
    dna_sequence = read_dna_sequence(dna_filename)

    str_sequences = list(dna_database[0].keys())[1:]  # Extract STRs from CSV header
    str_counts = {str_seq: longest_match(dna_sequence, str_seq) for str_seq in str_sequences}

    for person in dna_database:
        if all(str_counts[str_seq] == int(person[str_seq]) for str_seq in str_sequences):
            print(person['name'])
            return

    print("No match")

if __name__ == "__main__":
    main()