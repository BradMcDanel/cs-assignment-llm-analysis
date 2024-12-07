import csv
import sys

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    database_file = sys.argv[1]
    sequence_file = sys.argv[2]

    # Read the database file
    database = []
    str_names = []
    with open(database_file, 'r') as file:
        reader = csv.DictReader(file)
        str_names = reader.fieldnames[1:]  # Get STR names, excluding 'name'
        for row in reader:
            database.append(row)

    # Read the DNA sequence
    with open(sequence_file, 'r') as file:
        dna_sequence = file.read().strip()

    # Compute STR counts
    str_counts = {}
    for str_name in str_names:
        str_counts[str_name] = longest_match(dna_sequence, str_name)

    # Check database for matching profiles
    for person in database:
        if all(str_counts[str_name] == int(person[str_name]) for str_name in str_names):
            print(person['name'])
            return

    print("No match")

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
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