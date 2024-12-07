import csv
import sys

def read_csv(filename):
    """Read the CSV file and return a dictionary of people and their STR counts."""
    people = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            people[row['name']] = {key: int(value) for key, value in row.items() if key != 'name'}
    return people

def read_dna_sequence(filename):
    """Read the DNA sequence from a file and return it as a string."""
    with open(filename, 'r') as file:
        return file.read().strip()

def compute_longest_run(sequence, str):
    """Compute the longest run of consecutive repeats of the STR in the DNA sequence."""
    longest_run = 0
    for i in range(len(sequence)):
        count = 0
        while sequence[i:i+len(str)] == str:
            count += 1
            i += len(str)
        longest_run = max(longest_run, count)
    return longest_run

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    csv_file = sys.argv[1]
    sequence_file = sys.argv[2]

    people = read_csv(csv_file)
    dna_sequence = read_dna_sequence(sequence_file)

    # Get the list of STRs from the first person in the database
    strs = list(next(iter(people.values())).keys())

    # Compute the longest run for each STR
    str_counts = {str: compute_longest_run(dna_sequence, str) for str in strs}

    # Check for a match
    for name, profile in people.items():
        if all(profile[str] == str_counts[str] for str in strs):
            print(name)
            return

    print("No match")

if __name__ == "__main__":
    main()