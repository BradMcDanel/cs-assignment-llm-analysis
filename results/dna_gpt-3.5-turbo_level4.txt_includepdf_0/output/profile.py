import csv
import sys

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    # Get the file names from command line arguments
    csv_filename = sys.argv[1]
    dna_filename = sys.argv[2]

    # Read the CSV file into memory
    with open(csv_filename, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)
        data = {row[0]: [int(val) for val in row[1:]] for row in csv_reader}

    # Read the DNA sequence file into memory
    with open(dna_filename, "r") as dna_file:
        dna_sequence = dna_file.read()

    # Compute the longest run of consecutive repeats of each STR in the DNA sequence
    str_counts = {key: compute_str_count(dna_sequence, value) for key, value in data.items()}

    # Check for a match in the CSV data
    for name, counts in str_counts.items():
        if data[name] == counts:
            print(name)
            sys.exit(0)

    print("No match")

def compute_str_count(dna_sequence, str_pattern):
    count = 0
    max_count = 0
    str_length = len(str_pattern)
    for i in range(len(dna_sequence)):
        if dna_sequence[i:i + str_length] == str_pattern:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

if __name__ == "__main__":
    main()