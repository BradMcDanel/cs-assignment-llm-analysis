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

    # Read the DNA sequence file
    with open(sys.argv[2], 'r') as seqfile:
        sequence = seqfile.read().strip()

    # Get STR list from CSV header (excluding 'name')
    strs = list(database[0].keys())[1:]

    # Compute STR counts for the given DNA sequence
    str_counts = {}
    for str in strs:
        str_counts[str] = longest_match(sequence, str)

    # Check database for matching profiles
    for person in database:
        if all(str_counts[str] == int(person[str]) for str in strs):
            print(person['name'])
            return

    print("No match")

def longest_match(sequence, str):
    """Returns length of longest run of STR in DNA sequence."""
    longest = 0
    for i in range(len(sequence)):
        count = 0
        while True:
            start = i + count * len(str)
            if sequence[start:start+len(str)] == str:
                count += 1
            else:
                break
        longest = max(longest, count)
    return longest

if __name__ == "__main__":
    main()