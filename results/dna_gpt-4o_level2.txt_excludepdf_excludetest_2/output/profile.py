import csv
import sys

def load_database(csv_filename):
    """Load the DNA database from a CSV file."""
    with open(csv_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        database = [row for row in reader]
    return database

def load_dna_sequence(sequence_filename):
    """Load the DNA sequence from a text file."""
    with open(sequence_filename, 'r') as file:
        sequence = file.read().strip()
    return sequence

def longest_match(sequence, subsequence):
    """Returns length of longest run of `subsequence` in `sequence`."""
    longest_run = 0
    length = len(subsequence)
    
    for i in range(len(sequence)):
        # Check for the longest consecutive run of the subsequence
        count = 0
        while sequence[i:i + length] == subsequence:
            count += 1
            i += length
        
        longest_run = max(longest_run, count)

    return longest_run

def find_match(database, str_counts):
    """Find and return the name of the individual whose STR counts match."""
    for person in database:
        name = person['name']
        matches = all(int(person[str_name]) == str_counts[str_name] for str_name in str_counts)
        if matches:
            return name
    return "No match"

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return
    
    csv_filename = sys.argv[1]
    sequence_filename = sys.argv[2]
    
    database = load_database(csv_filename)
    sequence = load_dna_sequence(sequence_filename)
    
    str_names = database[0].keys() - {'name'}  # Extract STR names from the first row
    str_counts = {str_name: longest_match(sequence, str_name) for str_name in str_names}
    
    result = find_match(database, str_counts)
    print(result)

if __name__ == "__main__":
    main()