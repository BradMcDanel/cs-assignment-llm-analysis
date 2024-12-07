import sys
import csv

def load_database(filename):
    database = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            database.append(row)
    return database

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

    database_file = sys.argv[1]
    sequence_file = sys.argv[2]

    database = load_database(database_file)
    
    with open(sequence_file, 'r') as f:
        sequence = f.read().strip()

    strs = list(database[0].keys())[1:]  # Get STR names from CSV headers
    
    # Compute longest STR counts
    str_counts = {}
    for str_name in strs:
        str_counts[str_name] = longest_match(sequence, str_name)

    # Check database for matching profiles
    for person in database:
        if all(str_counts[str_name] == int(person[str_name]) for str_name in strs):
            print(person['name'])
            return

    print("No match")

if __name__ == "__main__":
    main()