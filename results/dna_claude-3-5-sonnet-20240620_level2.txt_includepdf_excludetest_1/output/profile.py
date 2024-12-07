import csv
import sys

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    # Read the database file
    database = []
    with open(sys.argv[1], 'r') as file:
        reader = csv.DictReader(file)
        database = list(reader)

    # Get the list of STRs from the header
    strs = list(database[0].keys())[1:]

    # Read the DNA sequence
    with open(sys.argv[2], 'r') as file:
        sequence = file.read().strip()

    # Compute the longest run of each STR in the sequence
    str_counts = {}
    for str in strs:
        str_counts[str] = longest_match(sequence, str)

    # Check if the counts match any individual in the database
    for person in database:
        if all(str_counts[str] == int(person[str]) for str in strs):
            print(person['name'])
            return

    print("No match")

def longest_match(sequence, subsequence):
    longest = 0
    length = len(subsequence)
    for i in range(len(sequence)):
        count = 0
        while sequence[i:i+length] == subsequence:
            count += 1
            i += length
        longest = max(longest, count)
    return longest

if __name__ == "__main__":
    main()