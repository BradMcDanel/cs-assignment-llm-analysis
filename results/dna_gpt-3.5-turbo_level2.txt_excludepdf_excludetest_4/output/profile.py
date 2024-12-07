import csv
import sys

# Read the CSV file
def read_csv(file_name):
    data = []
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

# Read the DNA sequence file
def read_dna_sequence(file_name):
    with open(file_name, 'r') as file:
        return file.read().replace('\n', '')

# Compute the longest run of consecutive repeats of the STR in the DNA sequence
def compute_str_counts(dna_sequence, str_sequence):
    max_count = 0
    current_count = 0
    str_length = len(str_sequence)
    
    for i in range(len(dna_sequence)):
        if dna_sequence[i:i+str_length] == str_sequence:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    
    return max_count

# Identify to whom the DNA belongs
def identify_dna_owner(csv_data, dna_sequence):
    for row in csv_data:
        str_counts = {}
        name = row['name']
        for key in row.keys():
            if key != 'name':
                str_counts[key] = compute_str_counts(dna_sequence, key)
        if all(int(row[key]) == str_counts[key] for key in str_counts):
            return name
    return "No match"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py <csv_file> <dna_sequence_file>")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    dna_sequence_file = sys.argv[2]
    
    csv_data = read_csv(csv_file)
    dna_sequence = read_dna_sequence(dna_sequence_file)
    
    result = identify_dna_owner(csv_data, dna_sequence)
    print(result)