import csv
import sys

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    # Read CSV file
    csv_file = sys.argv[1]
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = {row[0]: [int(x) for x in row[1:]] for row in reader}

    # Read DNA sequence file
    sequence_file = sys.argv[2]
    with open(sequence_file, 'r') as file:
        dna_sequence = file.read()

    # Find the longest consecutive repeats of each STR in the DNA sequence
    str_counts = {str_name: find_longest_str(dna_sequence, str_sequence) for str_name, str_sequence in data.items()}

    # Check for matching individual
    for name, counts in data.items():
        if counts == str_counts[name]:
            print(name)
            return

    print("No match")

def find_longest_str(dna_sequence, str_sequence):
    longest_run = 0
    current_run = 0
    str_length = len(str_sequence)
    
    for i in range(len(dna_sequence) - str_length):
        if dna_sequence[i:i + str_length] == str_sequence:
            current_run += 1
            longest_run = max(longest_run, current_run)
        else:
            current_run = 0

    return longest_run

if __name__ == "__main__":
    main()