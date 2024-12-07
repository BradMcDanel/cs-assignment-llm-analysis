import csv
import sys

def main():
    # Ensure correct usage
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    # Read the DNA database into memory from a CSV file
    database_filename = sys.argv[1]
    with open(database_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        database = list(reader)

    # Read the DNA sequence into memory from a text file
    sequence_filename = sys.argv[2]
    with open(sequence_filename, 'r') as file:
        dna_sequence = file.read().strip()

    # Extract the STRs from the database header
    str_sequences = reader.fieldnames[1:]

    # For each STR, compute the longest run in the DNA sequence
    str_counts = {}
    for str_seq in str_sequences:
        str_counts[str_seq] = longest_run(dna_sequence, str_seq)

    # Check database for matching profiles
    for person in database:
        if all(str_counts[str_seq] == int(person[str_seq]) for str_seq in str_sequences):
            print(person['name'])
            return

    print("No match")

def longest_run(sequence, str_seq):
    """Returns the longest run of consecutive repeats of str_seq in sequence."""
    max_run = 0
    str_len = len(str_seq)
    seq_len = len(sequence)

    for i in range(seq_len):
        # Count runs of str_seq starting at position i
        count = 0
        while sequence[i:i + str_len] == str_seq:
            count += 1
            i += str_len

        # Update max_run if current count is greater
        max_run = max(max_run, count)

    return max_run

if __name__ == "__main__":
    main()