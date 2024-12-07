import csv
import sys

def read_csv_file(csv_filename):
    # Open the CSV file and read its contents
    with open(csv_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
        return data

def read_dna_sequence(dna_filename):
    # Open the DNA sequence file and read its contents
    with open(dna_filename, 'r') as file:
        sequence = file.read().strip()
    return sequence

def longest_match(sequence, subsequence):
    # Initialize variables
    longest_run = 0
    sub_len = len(subsequence)
    seq_len = len(sequence)

    # Check each position in sequence for most consecutive runs of subsequence
    for i in range(seq_len):
        count = 0

        # Continue until no more consecutive matches
        while True:
            # Adjust start and end according to current count
            start = i + count * sub_len
            end = start + sub_len

            # If there's a match, increase count
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        # Update the longest run found
        longest_run = max(longest_run, count)

    return longest_run

def find_matching_profile(dna_database, str_counts):
    # Compare each profile in the database against the STR counts
    for profile in dna_database:
        match = True
        for str_name, count in str_counts.items():
            if int(profile[str_name]) != count:
                match = False
                break
        if match:
            return profile['name']
    return "No match"

def main():
    # Check command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    # Read the DNA database and sequence
    csv_filename = sys.argv[1]
    dna_filename = sys.argv[2]
    dna_database = read_csv_file(csv_filename)
    dna_sequence = read_dna_sequence(dna_filename)

    # Extract STRs from the database header
    str_sequences = list(dna_database[0].keys())[1:]

    # Compute the longest match for each STR
    str_counts = {str_seq: longest_match(dna_sequence, str_seq) for str_seq in str_sequences}

    # Determine which profile matches the STR counts
    matching_profile = find_matching_profile(dna_database, str_counts)
    print(matching_profile)

if __name__ == "__main__":
    main()