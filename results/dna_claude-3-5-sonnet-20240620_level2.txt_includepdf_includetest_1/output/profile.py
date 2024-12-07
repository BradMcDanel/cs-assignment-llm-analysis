import csv
import sys

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

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python profile.py data.csv sequence.txt")

    # Read database file into a variable
    database = []
    with open(sys.argv[1], 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            database.append(row)

    # Read DNA sequence file into a variable
    with open(sys.argv[2], 'r') as file:
        dna_sequence = file.read()

    # Find longest match of each STR in DNA sequence
    str_counts = {}
    for key in database[0].keys():
        if key != 'name':
            str_counts[key] = longest_match(dna_sequence, key)

    # Check database for matching profiles
    for person in database:
        if all(str_counts[str] == int(person[str]) for str in str_counts):
            print(person['name'])
            return

    print("No match")

if __name__ == "__main__":
    main()