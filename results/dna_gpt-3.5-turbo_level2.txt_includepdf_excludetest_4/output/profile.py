import csv
import sys

# Read CSV file
csv_file = sys.argv[1]
with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    headers = csv_reader.fieldnames
    data = [row for row in csv_reader]

# Read DNA sequence file
dna_file = sys.argv[2]
with open(dna_file, 'r') as file:
    dna_sequence = file.read()

# Compute longest run of consecutive repeats for each STR
matches = []
for row in data:
    name = row['name']
    str_counts = {header: int(row[header]) for header in headers[1:]}
    str_lengths = {}
    
    for str_name, str_count in str_counts.items():
        longest_run = 0
        current_run = 0
        str_len = len(str_name)
        
        for i in range(len(dna_sequence) - str_len):
            if dna_sequence[i:i+str_len] == str_name:
                current_run += 1
            else:
                longest_run = max(longest_run, current_run)
                current_run = 0
        
        str_lengths[str_name] = longest_run
    
    if str_lengths == str_counts:
        matches.append(name)

# Print matching individual or "No match"
if matches:
    print(matches[0])
else:
    print("No match")