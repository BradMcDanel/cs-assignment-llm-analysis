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

    # Get STR names from CSV header
    strs = list(database[0].keys())[1:]

    # Read the DNA sequence
    with open(sys.argv[2], 'r') as sequence_file:
        sequence = sequence_file.read().strip()

    # Compute STR counts
    str_counts = {}
    for str_name in strs:
        str_counts[str_name] = longest_match(sequence, str_name)

    # Check for matching profiles
    for person in database:
        if all(str_counts[str_name] == int(person[str_name]) for str_name in strs):
            print(person['name'])
            return

    print("No match")

def longest_match(sequence, subsequence):
    longest = 0
    current = 0
    subsequence_length = len(subsequence)
    
    for i in range(len(sequence)):
        if sequence[i:i+subsequence_length] == subsequence:
            current += 1
            if current > longest:
                longest = current
        else:
            current = 0
    
    return longest

if __name__ == "__main__":
    main()