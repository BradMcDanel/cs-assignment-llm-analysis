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

    # Read the DNA sequence
    with open(sys.argv[2], 'r') as sequencefile:
        sequence = sequencefile.read().strip()

    # Get the list of STRs from the CSV header
    strs = list(database[0].keys())[1:]

    # Compute the longest run of each STR in the sequence
    str_counts = {}
    for str in strs:
        str_counts[str] = longest_match(sequence, str)

    # Check if the STR counts match any individual in the database
    for person in database:
        if all(str_counts[str] == int(person[str]) for str in strs):
            print(person['name'])
            return

    # If no match is found
    print("No match")

def longest_match(sequence, str):
    """Returns length of longest run of str in sequence."""
    longest_run = 0
    for i in range(len(sequence)):
        count = 0
        while True:
            start = i + count * len(str)
            chunk = sequence[start:start + len(str)]
            if chunk == str:
                count += 1
            else:
                break
        longest_run = max(longest_run, count)
    return longest_run

if __name__ == "__main__":
    main()