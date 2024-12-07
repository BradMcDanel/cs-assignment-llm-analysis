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
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    csv_file = sys.argv[1]
    dna_file = sys.argv[2]

    # Read database file into a dictionary
    database = {}
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            database[row['name']] = {key: int(value) for key, value in row.items() if key != 'name'}

    # Read DNA sequence
    with open(dna_file, 'r') as file:
        dna_sequence = file.read().strip()

    # Find longest match of each STR in DNA sequence
    str_counts = {}
    for str_sequence in database[next(iter(database))].keys():
        str_counts[str_sequence] = longest_match(dna_sequence, str_sequence)

    # Check database for matching profiles
    for name, profile in database.items():
        if all(str_counts[str_sequence] == count for str_sequence, count in profile.items()):
            print(name)
            return

    print("No match")

if __name__ == "__main__":
    main()