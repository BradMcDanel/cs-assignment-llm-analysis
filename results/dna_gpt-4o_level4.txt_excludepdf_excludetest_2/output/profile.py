import csv
import sys

def read_csv(filename):
    """Reads the CSV file and extracts the STR headers and database."""
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        str_headers = reader.fieldnames[1:]  # Exclude the 'name' field
        database = list(reader)
    return str_headers, database

def read_dna_sequence(filename):
    """Reads the DNA sequence from a text file."""
    with open(filename, 'r') as file:
        sequence = file.read().strip()
    return sequence

def longest_match(sequence, subsequence):
    """Returns length of the longest run of subsequence in sequence."""
    longest_run = 0
    sub_len = len(subsequence)
    seq_len = len(sequence)
    
    for i in range(seq_len):
        # Count consecutive runs of subsequence
        count = 0
        while (i + count * sub_len < seq_len) and (sequence[i + count * sub_len:i + (count + 1) * sub_len] == subsequence):
            count += 1
        # Update max run length
        longest_run = max(longest_run, count)
    
    return longest_run

def find_matching_individual(database, str_counts):
    """Finds and returns the name of the individual whose STR counts match."""
    for person in database:
        # Check if the person's STR counts match the computed counts
        if all(int(person[str_name]) == str_counts[str_name] for str_name in str_counts):
            return person['name']
    return "No match"

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return
    
    csv_filename = sys.argv[1]
    sequence_filename = sys.argv[2]
    
    # Read the CSV file and DNA sequence
    str_headers, database = read_csv(csv_filename)
    sequence = read_dna_sequence(sequence_filename)
    
    # Compute the longest run of each STR in the DNA sequence
    str_counts = {str_name: longest_match(sequence, str_name) for str_name in str_headers}
    
    # Find and print the matching individual's name
    result = find_matching_individual(database, str_counts)
    print(result)

if __name__ == "__main__":
    main()