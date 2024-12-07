import csv
import sys

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    # Read CSV file into memory
    database = []
    with open(sys.argv[1], 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            database.append(row)

    # Read DNA sequence file
    with open(sys.argv[2], 'r') as sequence_file:
        sequence = sequence_file.read().strip()

    # Get list of STRs from CSV header (excluding 'name')
    strs = list(database[0].keys())[1:]

    # Compute longest run of consecutive repeats for each STR
    str_counts = {}
    for str_sequence in strs:
        str_counts[str_sequence] = longest_match(sequence, str_sequence)

    # Check database for matching profiles
    for person in database:
        if all(str_counts[str_sequence] == int(person[str_sequence]) for str_sequence in strs):
            print(person['name'])
            return

    # If no match found
    print("No match")

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

if __name__ == "__main__":
    main()