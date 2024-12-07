import csv
import sys

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
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    # Read database file into a variable
    database_file = sys.argv[1]
    with open(database_file) as f:
        reader = csv.DictReader(f)
        database = list(reader)

    # Read DNA sequence file into a variable
    sequence_file = sys.argv[2]
    with open(sequence_file) as f:
        sequence = f.read().strip()

    # Find longest match of each STR in DNA sequence
    strs = list(database[0].keys())[1:]  # Get STR names from database
    str_counts = {}
    for str_name in strs:
        str_counts[str_name] = longest_match(sequence, str_name)

    # Check database for matching profiles
    for person in database:
        match = True
        for str_name in strs:
            if int(person[str_name]) != str_counts[str_name]:
                match = False
                break
        if match:
            print(person['name'])
            return

    print("No match")

if __name__ == "__main__":
    main()