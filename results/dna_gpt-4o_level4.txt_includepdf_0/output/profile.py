import csv
import sys

def load_csv(filename):
    """Load the CSV file and return the data."""
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

def load_dna_sequence(filename):
    """Load the DNA sequence from the text file."""
    with open(filename, 'r') as file:
        sequence = file.read().strip()
    return sequence

def longest_match(sequence, subsequence):
    """Compute the longest run of consecutive repeats of subsequence in sequence."""
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

    csv_filename = sys.argv[1]
    dna_filename = sys.argv[2]

    database = load_csv(csv_filename)
    dna_sequence = load_dna_sequence(dna_filename)

    str_counts = {}
    for str_sequence in database[0].keys():
        if str_sequence != "name":
            str_counts[str_sequence] = longest_match(dna_sequence, str_sequence)

    for person in database:
        match = True
        for str_sequence in str_counts:
            if int(person[str_sequence]) != str_counts[str_sequence]:
                match = False
                break
        if match:
            print(person["name"])
            return

    print("No match")

if __name__ == "__main__":
    main()