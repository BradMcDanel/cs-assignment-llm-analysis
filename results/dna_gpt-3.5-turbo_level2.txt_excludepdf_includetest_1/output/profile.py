import csv
import sys

def main():
    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    # Read the CSV file
    csv_filename = sys.argv[1]
    with open(csv_filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        str_counts = {row[0]: row[1:] for row in csvreader}

    # Read the DNA sequence file
    dna_filename = sys.argv[2]
    with open(dna_filename, 'r') as dnafile:
        dna_sequence = dnafile.read()

    # Compute the longest run of consecutive repeats of each STR in the DNA sequence
    longest_runs = {}
    for str_type in header[1:]:
        longest_run = 0
        current_run = 0
        str_len = len(str_type)
        for i in range(len(dna_sequence) - str_len):
            if dna_sequence[i:i + str_len] == str_type:
                current_run += 1
                if current_run > longest_run:
                    longest_run = current_run
            else:
                current_run = 0
        longest_runs[str_type] = longest_run

    # Compare the computed STR counts with individuals in the CSV file
    for name, counts in str_counts.items():
        if all(int(counts[i]) == longest_runs[str_type] for i, str_type in enumerate(header[1:])):
            print(name)
            sys.exit(0)

    print("No match")

if __name__ == "__main__":
    main()