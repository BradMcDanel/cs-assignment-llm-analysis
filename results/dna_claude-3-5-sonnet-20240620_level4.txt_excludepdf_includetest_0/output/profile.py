import csv
import sys

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    # Read the CSV file into memory
    database = {}
    with open(sys.argv[1], 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            database[row['name']] = {key: int(value) for key, value in row.items() if key != 'name'}

    # Read the DNA sequence
    with open(sys.argv[2], 'r') as sequence_file:
        sequence = sequence_file.read().strip()

    # Compute STR counts
    str_counts = {}
    for str_name in database[next(iter(database))].keys():
        str_counts[str_name] = longest_match(sequence, str_name)

    # Check for matching profiles
    for name, profile in database.items():
        if all(str_counts[str_name] == count for str_name, count in profile.items()):
            print(name)
            return

    print("No match")

def longest_match(sequence, str):
    """Returns length of longest run of str in sequence."""
    longest_run = 0
    str_length = len(str)
    for i in range(len(sequence)):
        count = 0
        while sequence[i:i+str_length] == str:
            count += 1
            i += str_length
        longest_run = max(longest_run, count)
    return longest_run

if __name__ == "__main__":
    main()