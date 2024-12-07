import sys
import csv

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
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
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python profile.py data.csv sequence.txt")

    # Read the CSV file into memory
    database = []
    with open(sys.argv[1], 'r') as file:
        reader = csv.DictReader(file)
        database = list(reader)

    # Read DNA sequence file into a string
    with open(sys.argv[2], 'r') as file:
        dna_sequence = file.read().strip()

    # Find longest match of each STR in DNA sequence
    str_counts = {}
    for key in database[0].keys():
        if key != 'name':
            str_counts[key] = longest_match(dna_sequence, key)

    # Check database for matching profiles
    for person in database:
        if all(str_counts[str] == int(person[str]) for str in str_counts):
            print(person['name'])
            return

    print("No match")

if __name__ == "__main__":
    main()