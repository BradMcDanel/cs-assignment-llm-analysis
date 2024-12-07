import csv
import sys

# Read CSV file
def read_csv(filename):
    data = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data[row['name']] = {k: int(v) for k, v in row.items() if k != 'name'}
    return data

# Read DNA sequence
def read_dna(filename):
    with open(filename, 'r') as file:
        return file.read()

# Compute longest run of consecutive repeats
def compute_str_counts(dna, str_sequence):
    max_count = 0
    current_count = 0
    str_length = len(str_sequence)
    
    for i in range(len(dna) - str_length):
        if dna[i:i+str_length] == str_sequence:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
            
    return max_count

# Main program
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)
    
    data_file = sys.argv[1]
    sequence_file = sys.argv[2]
    
    data = read_csv(data_file)
    dna_sequence = read_dna(sequence_file)
    
    for person, str_counts in data.items():
        matches = [compute_str_counts(dna_sequence, str_sequence) == count for str_sequence, count in str_counts.items()]
        if all(matches):
            print(person)
            sys.exit(0)
    
    print("No match")