import csv
import sys

def read_database(file_path):
    """Reads the CSV database file into a list of dictionaries."""
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def read_dna_sequence(file_path):
    """Reads the DNA sequence file into a string."""
    with open(file_path, 'r') as file:
        return file.read().strip()

def longest_match(sequence, subsequence):
    """Returns the length of the longest run of subsequence in sequence."""
    longest_run = 0
    sub_len = len(subsequence)
    
    for i in range(len(sequence)):
        count = 0
        while sequence[i:i + sub_len] == subsequence:
            count += 1
            i += sub_len
        longest_run = max(longest_run, count)
    
    return longest_run

def find_dna_match(database, dna_sequence, str_sequences):
    """Finds the person who matches the DNA STR counts."""
    # Calculate the longest match for each STR
    str_counts = {str_seq: longest_match(dna_sequence, str_seq) for str_seq in str_sequences}
    
    # Compare against each person in the database
    for person in database:
        if all(int(person[str_seq]) == count for str_seq, count in str_counts.items()):
            return person["name"]
    return "No match"

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)
    
    database_path = sys.argv[1]
    dna_sequence_path = sys.argv[2]
    
    # Read the database and DNA sequence
    database = read_database(database_path)
    dna_sequence = read_dna_sequence(dna_sequence_path)
    
    # Get the list of STRs from the database
    str_sequences = database[0].keys()
    str_sequences.remove("name")
    
    # Find and print the match
    match = find_dna_match(database, dna_sequence, str_sequences)
    print(match)

if __name__ == "__main__":
    main()