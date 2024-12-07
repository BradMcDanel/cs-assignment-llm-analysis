import csv
import sys

def read_database(filename):
    """Reads the DNA database from a CSV file."""
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        database = list(reader)
    return database

def read_dna_sequence(filename):
    """Reads the DNA sequence from a text file."""
    with open(filename, 'r') as file:
        sequence = file.read().strip()
    return sequence

def longest_match(sequence, subsequence):
    """Returns the longest run of subsequence in sequence."""
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)
    
    for i in range(sequence_length):
        count = 0
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        longest_run = max(longest_run, count)
    
    return longest_run

def find_matching_profile(database, str_counts):
    """Finds the individual in the database that matches the given STR counts."""
    for person in database:
        match = True
        for str_name, count in str_counts.items():
            if int(person[str_name]) != count:
                match = False
                break
        if match:
            return person['name']
    return "No match"

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    database_file = sys.argv[1]
    sequence_file = sys.argv[2]

    database = read_database(database_file)
    sequence = read_dna_sequence(sequence_file)
    
    # Extract STRs from the database's first row
    strs = database[0].keys()
    strs = list(strs)[1:]  # Skip the 'name' column

    # Calculate longest match of each STR in the sequence
    str_counts = {}
    for str_sequence in strs:
        str_counts[str_sequence] = longest_match(sequence, str_sequence)
    
    # Find and output matching profile
    match = find_matching_profile(database, str_counts)
    print(match)

if __name__ == "__main__":
    main()