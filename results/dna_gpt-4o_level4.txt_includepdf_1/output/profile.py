import csv
import sys

def load_csv(filename):
    """Loads the CSV file and returns the header and data as lists."""
    with open(filename, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [row for row in reader]
    return header, data

def load_dna_sequence(filename):
    """Loads the DNA sequence from the text file."""
    with open(filename, "r") as file:
        return file.read().strip()

def longest_run(sequence, subsequence):
    """Finds the longest run of the subsequence in the sequence."""
    max_run = 0
    n = len(subsequence)
    for i in range(len(sequence)):
        run_length = 0
        while sequence[i:i + n] == subsequence:
            run_length += 1
            i += n
        max_run = max(max_run, run_length)
    return max_run

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return
    
    csv_file = sys.argv[1]
    sequence_file = sys.argv[2]

    # Load CSV and DNA sequence
    header, data = load_csv(csv_file)
    dna_sequence = load_dna_sequence(sequence_file)

    # Extract STRs from header
    strs = header[1:]

    # Compute the longest run for each STR in the DNA sequence
    longest_runs = [longest_run(dna_sequence, str_seq) for str_seq in strs]

    # Compare with each individual in the database
    for person in data:
        name = person[0]
        counts = list(map(int, person[1:]))
        if counts == longest_runs:
            print(name)
            return

    print("No match")

if __name__ == "__main__":
    main()