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
    with open(sys.argv[1], 'r') as file:
        reader = csv.DictReader(file)
        database = list(reader)
        strs = reader.fieldnames[1:]

    # Read DNA sequence file into a variable
    with open(sys.argv[2], 'r') as file:
        sequence = file.read()

    # Find longest match of each STR in DNA sequence
    profile = {}
    for str_sequence in strs:
        profile[str_sequence] = longest_match(sequence, str_sequence)

    # Check database for matching profiles
    for person in database:
        if all(int(person[str_sequence]) == profile[str_sequence] for str_sequence in strs):
            print(person['name'])
            return

    print("No match")

if __name__ == "__main__":
    main()