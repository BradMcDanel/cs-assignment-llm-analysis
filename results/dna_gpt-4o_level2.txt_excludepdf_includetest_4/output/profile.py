import csv
import sys

def longest_match(sequence, subsequence):
    """Returns the longest run of subsequence in sequence."""
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

    # Read database file into memory
    csv_file = sys.argv[1]
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        str_names = reader.fieldnames[1:]
        people = [row for row in reader]

    # Read DNA sequence file into memory
    sequence_file = sys.argv[2]
    with open(sequence_file) as file:
        dna_sequence = file.read().strip()

    # Compute longest match of each STR in the DNA sequence
    str_counts = {str_name: longest_match(dna_sequence, str_name) for str_name in str_names}

    # Check database for matching profile
    for person in people:
        match = all(str_counts[str_name] == int(person[str_name]) for str_name in str_names)
        if match:
            print(person['name'])
            return

    print("No match")

if __name__ == "__main__":
    main()