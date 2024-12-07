import csv
import sys

# Function to calculate the longest run of consecutive repeats of an STR in the DNA sequence
def calculate_longest_run(sequence, str_sequence):
    longest_run = 0
    current_run = 0
    str_len = len(str_sequence)
    
    for i in range(len(sequence)):
        if sequence[i:i+str_len] == str_sequence:
            current_run += 1
            if current_run > longest_run:
                longest_run = current_run
        else:
            current_run = 0
            
    return longest_run

# Read CSV file
csv_filename = sys.argv[1]
with open(csv_filename, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    headers = next(csv_reader)
    rows = list(csv_reader)

# Read DNA sequence
dna_filename = sys.argv[2]
with open(dna_filename, 'r') as dna_file:
    dna_sequence = dna_file.read()

# Iterate through each individual in the CSV file
for row in rows:
    name = row[0]
    strs = row[1:]

    # Calculate the longest run for each STR in the DNA sequence
    longest_runs = [calculate_longest_run(dna_sequence, str_sequence) for str_sequence in strs]

    # Check if the STR counts match exactly with any individual
    if longest_runs == list(map(int, strs)):
        print(name)
        sys.exit()

# If no match found
print("No match")