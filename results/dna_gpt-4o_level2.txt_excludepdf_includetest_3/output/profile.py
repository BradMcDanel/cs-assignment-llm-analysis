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

def load_dna_database(filename):
    """Loads the DNA database from a CSV file and returns a list of dictionaries."""
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def load_dna_sequence(filename):
    """Loads the DNA sequence from a text file."""
    with open(filename) as file:
        return file.read().strip()

def find_match(database, sequence, str_sequences):
    """Finds a matching individual in the database for the given DNA sequence."""
    str_counts = {str_seq: longest_match(sequence, str_seq) for str_seq in str_sequences}

    for person in database:
        if all(int(person[str_seq]) == str_counts[str_seq] for str_seq in str_sequences):
            return person['name']
    return "No match"

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return

    database_filename = sys.argv[1]
    sequence_filename = sys.argv[2]

    database = load_dna_database(database_filename)
    sequence = load_dna_sequence(sequence_filename)
    str_sequences = database[0].keys() - {'name'}

    match = find_match(database, sequence, str_sequences)
    print(match)

if __name__ == "__main__":
    main()