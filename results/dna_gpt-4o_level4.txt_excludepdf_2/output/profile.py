import csv
import sys

def read_csv(filename):
    """Reads the CSV file and returns the header and the list of individuals with their STR counts."""
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        header = reader.fieldnames
        data = list(reader)
    return header, data

def read_dna_sequence(filename):
    """Reads the DNA sequence from a text file and returns it as a string."""
    with open(filename, 'r') as file:
        return file.read().strip()

def longest_match(sequence, subsequence):
    """Returns the longest run of consecutive repeats of subsequence in sequence."""
    longest_run = 0
    sub_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        count = 0
        while sequence[i + count*sub_len : i + (count+1)*sub_len] == subsequence:
            count += 1
        longest_run = max(longest_run, count)

    return longest_run

def find_matching_individual(header, individuals, str_counts):
    """Finds and returns the name of the individual whose STR counts match the given str_counts."""
    for individual in individuals:
        if all(int(individual[str]) == str_counts[str] for str in str_counts):
            return individual['name']
    return "No match"

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    csv_filename = sys.argv[1]
    dna_filename = sys.argv[2]

    # Step 1: Read the CSV file and DNA sequence
    header, individuals = read_csv(csv_filename)
    dna_sequence = read_dna_sequence(dna_filename)

    # Step 2: Compute the longest run of consecutive repeats for each STR
    str_counts = {}
    for str in header[1:]:  # Skip the first column 'name'
        str_counts[str] = longest_match(dna_sequence, str)

    # Step 3: Find the matching individual
    match = find_matching_individual(header, individuals, str_counts)
    print(match)

if __name__ == "__main__":
    main()