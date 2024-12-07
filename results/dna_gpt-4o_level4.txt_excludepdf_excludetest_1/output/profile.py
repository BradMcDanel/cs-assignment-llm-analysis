import csv
import sys

def read_csv(filename):
    # Open the CSV file and read its contents
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        people = list(reader)
    return people

def read_dna_sequence(filename):
    # Open the DNA sequence file and read its contents
    with open(filename) as file:
        sequence = file.read().strip()
    return sequence

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    longest_run = 0
    subseq_length = len(subsequence)
    seq_length = len(sequence)

    for i in range(seq_length):
        # Check for a subsequence match in a "window" of sequence
        count = 0
        while True:
            start = i + count * subseq_length
            end = start + subseq_length
            # If there's a match in the current window, keep checking
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        # Update the longest run found
        longest_run = max(longest_run, count)
    return longest_run

def find_matching_profile(people, str_counts):
    # Compare the STR counts against each individual's profile
    for person in people:
        # Assume a match until we find a non-matching STR count
        match = True
        for str_name, count in str_counts.items():
            if int(person[str_name]) != count:
                match = False
                break
        if match:
            return person['name']
    return "No match"

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python profile.py data.csv sequence.txt")

    # Read the database and DNA sequence
    people = read_csv(sys.argv[1])
    dna_sequence = read_dna_sequence(sys.argv[2])

    # Get STRs from the first row of the CSV
    str_names = people[0].keys() - {'name'}

    # Compute longest match for each STR
    str_counts = {str_name: longest_match(dna_sequence, str_name) for str_name in str_names}

    # Find and print the matching profile
    match = find_matching_profile(people, str_counts)
    print(match)

if __name__ == "__main__":
    main()