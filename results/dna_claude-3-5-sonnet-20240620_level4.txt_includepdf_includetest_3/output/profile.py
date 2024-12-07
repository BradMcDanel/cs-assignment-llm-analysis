import sys
import csv

def load_database(filename):
    database = {}
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            database[row['name']] = {key: int(value) for key, value in row.items() if key != 'name'}
    return database

def load_sequence(filename):
    with open(filename, 'r') as f:
        return f.read().strip()

def count_longest_str(sequence, str):
    longest = 0
    current = 0
    i = 0
    while i < len(sequence):
        if sequence[i:i+len(str)] == str:
            current += 1
            i += len(str)
        else:
            longest = max(longest, current)
            current = 0
            i += 1
    return max(longest, current)

def profile_dna(database, sequence):
    str_counts = {str: count_longest_str(sequence, str) for str in next(iter(database.values())).keys()}
    
    for name, profile in database.items():
        if all(str_counts[str] == count for str, count in profile.items()):
            return name
    
    return "No match"

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    database_file = sys.argv[1]
    sequence_file = sys.argv[2]

    database = load_database(database_file)
    sequence = load_sequence(sequence_file)

    result = profile_dna(database, sequence)
    print(result)

if __name__ == "__main__":
    main()