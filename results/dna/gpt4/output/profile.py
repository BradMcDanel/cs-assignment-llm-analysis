import csv
import sys

def read_csv(filename):
    """Reads a CSV file and returns a header list and a list of dictionaries for each row."""
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
        return reader.fieldnames, data

def read_dna_sequence(filename):
    """Reads a DNA sequence from a text file."""
    with open(filename, 'r') as file:
        return file.read().strip()

def longest_run(sequence, substring):
    """Finds the longest run of a substring in a sequence."""
    max_run = 0
    i = 0
    while i < len(sequence):
        current_run = 0
        while sequence[i:i+len(substring)] == substring:
            current_run += 1
            i += len(substring)
        max_run = max(max_run, current_run)
        i += 1 if current_run == 0 else 0
    return max_run

def match_dna(data, str_counts):
    """Compares STR counts with each individual's STR counts in the data."""
    for person in data:
        if all(person[str_name] == str(count) for str_name, count in str_counts.items()):
            return person['name']
    return "No match"

def main(csv_filename, dna_filename):
    headers, data = read_csv(csv_filename)
    dna_sequence = read_dna_sequence(dna_filename)
    str_counts = {str_name: longest_run(dna_sequence, str_name) for str_name in headers if str_name != 'name'}
    
    result = match_dna(data, str_counts)
    print(result)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    csv_filename = sys.argv[1]
    dna_filename = sys.argv[2]
    main(csv_filename, dna_filename)