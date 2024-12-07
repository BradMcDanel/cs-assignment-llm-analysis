import csv
import sys

# Read CSV file
csv_filename = sys.argv[1]
with open(csv_filename, newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        name = row['name']
        str_counts = {key: int(value) for key, value in row.items() if key != 'name'}

# Read DNA sequence
dna_filename = sys.argv[2]
with open(dna_filename, 'r') as dna_file:
    dna_sequence = dna_file.read()

# Compute longest run of consecutive repeats of each STR
max_counts = {}
for str_key in str_counts:
    str_len = len(str_key)
    max_count = 0
    current_count = 0
    for i in range(len(dna_sequence) - str_len):
        if dna_sequence[i:i+str_len] == str_key:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0
    max_counts[str_key] = max_count

# Check for matching individual
for name, counts in str_counts.items():
    if counts == max_counts.values():
        print(name)
        break
else:
    print("No match")