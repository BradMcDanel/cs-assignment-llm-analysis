import csv
import sys

# Read the CSV file
csv_file = sys.argv[1]
with open(csv_file, mode='r') as file:
    csv_reader = csv.DictReader(file)
    data = [row for row in csv_reader]

# Read the DNA sequence file
sequence_file = sys.argv[2]
with open(sequence_file, mode='r') as file:
    dna_sequence = file.read()

# Function to compute the longest run of consecutive repeats of a substring
def longest_run(sequence, substring):
    max_run = 0
    current_run = 0
    index = 0
    while index < len(sequence):
        if sequence[index:index+len(substring)] == substring:
            current_run += 1
            index += len(substring)
        else:
            max_run = max(max_run, current_run)
            current_run = 0
            index += 1
    max_run = max(max_run, current_run)
    return max_run

# Compare the STR counts with individuals in the CSV file
for row in data:
    name = row['name']
    str_counts = {key: int(value) for key, value in row.items() if key != 'name'}
    match = True
    for str_name, count in str_counts.items():
        if longest_run(dna_sequence, str_name) != count:
            match = False
            break
    if match:
        print(name)
        sys.exit()

print("No match")