import csv
import sys

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    # Read the CSV file into memory
    database = []
    with open(sys.argv[1], 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            database.append(row)
    
    # Get the list of STRs from the CSV header
    strs = list(database[0].keys())[1:]

    # Read the DNA sequence
    with open(sys.argv[2], 'r') as sequencefile:
        sequence = sequencefile.read().strip()

    # Compute the longest run of each STR in the sequence
    str_counts = {}
    for str_seq in strs:
        str_counts[str_seq] = longest_match(sequence, str_seq)

    # Check if the STR counts match any individual in the database
    for person in database:
        if all(str_counts[str_seq] == int(person[str_seq]) for str_seq in strs):
            print(person['name'])
            return

    # If no match is found
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