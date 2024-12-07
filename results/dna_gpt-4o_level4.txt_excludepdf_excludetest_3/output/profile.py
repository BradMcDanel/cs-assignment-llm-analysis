import csv
import sys

def read_csv_file(csv_filename):
    """Reads the CSV file and returns a list of individuals with their STR counts."""
    with open(csv_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        individuals = []
        for row in reader:
            individuals.append(row)
    return individuals

def read_dna_sequence(sequence_filename):
    """Reads the DNA sequence file and returns the DNA sequence as a string."""
    with open(sequence_filename, 'r') as file:
        sequence = file.read().strip()
    return sequence

def longest_match(sequence, subsequence):
    """Finds the longest run of a subsequence in the sequence."""
    longest_run = 0
    subseq_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        count = 0
        while (i + count * subseq_len) < seq_len and sequence[i + count * subseq_len: i + (count + 1) * subseq_len] == subsequence:
            count += 1
        longest_run = max(longest_run, count)

    return longest_run

def find_matching_individual(individuals, str_counts):
    """Finds the individual whose STR counts match the given str_counts."""
    for person in individuals:
        if all(int(person[str_name]) == str_counts[str_name] for str_name in str_counts):
            return person['name']
    return "No match"

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return

    csv_filename = sys.argv[1]
    sequence_filename = sys.argv[2]

    # Read the CSV file into a list of individuals
    individuals = read_csv_file(csv_filename)

    # Read the DNA sequence
    dna_sequence = read_dna_sequence(sequence_filename)

    # Extract STR names from the CSV header
    str_names = list(individuals[0].keys())[1:]

    # Compute the longest match of each STR in the DNA sequence
    str_counts = {str_name: longest_match(dna_sequence, str_name) for str_name in str_names}

    # Find the individual with matching STR counts
    matching_individual = find_matching_individual(individuals, str_counts)

    # Print the result
    print(matching_individual)

if __name__ == "__main__":
    main()