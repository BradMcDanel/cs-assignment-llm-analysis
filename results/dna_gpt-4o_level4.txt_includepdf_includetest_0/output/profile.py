import csv
import sys

def read_csv_file(filename):
    """
    Read the CSV file and return the header and a list of individuals with their STR counts.
    """
    with open(filename) as file:
        reader = csv.DictReader(file)
        str_sequences = reader.fieldnames[1:]  # Extract STR names from the header
        individuals = [row for row in reader]
    return str_sequences, individuals

def read_sequence_file(filename):
    """
    Read the DNA sequence from a text file and return it as a string.
    """
    with open(filename) as file:
        return file.read()

def longest_match(sequence, subsequence):
    """
    Compute the longest run of consecutive repeats of subsequence in the DNA sequence.
    """
    longest_run = 0
    sub_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        count = 0
        while True:
            start = i + count * sub_len
            end = start + sub_len
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

    csv_filename = sys.argv[1]
    sequence_filename = sys.argv[2]

    str_sequences, individuals = read_csv_file(csv_filename)
    dna_sequence = read_sequence_file(sequence_filename)

    # Compute the longest match for each STR
    str_counts = {str_sequence: longest_match(dna_sequence, str_sequence) for str_sequence in str_sequences}

    # Compare the computed STR counts against each individual in the database
    for person in individuals:
        if all(str_counts[str_sequence] == int(person[str_sequence]) for str_sequence in str_sequences):
            print(person['name'])
            return

    print("No match")

if __name__ == "__main__":
    main()