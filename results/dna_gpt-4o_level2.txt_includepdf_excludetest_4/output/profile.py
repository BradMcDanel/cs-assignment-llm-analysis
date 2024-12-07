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
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    database_filename = sys.argv[1]
    sequence_filename = sys.argv[2]

    # Read database into memory
    with open(database_filename) as file:
        reader = csv.DictReader(file)
        database = list(reader)

    # Read DNA sequence into memory
    with open(sequence_filename) as file:
        dna_sequence = file.read().strip()

    # Get STRs from the first row of the CSV file
    str_sequences = reader.fieldnames[1:]

    # Find longest match of each STR in DNA sequence
    str_counts = {str_seq: longest_match(dna_sequence, str_seq) for str_seq in str_sequences}

    # Check database for matching profiles
    for person in database:
        if all(int(person[str_seq]) == str_counts[str_seq] for str_seq in str_sequences):
            print(person['name'])
            return

    print("No match")

if __name__ == "__main__":
    main()