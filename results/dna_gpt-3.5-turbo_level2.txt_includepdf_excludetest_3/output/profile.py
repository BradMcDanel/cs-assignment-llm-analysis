import csv
import sys

# Read CSV file
csv_file = sys.argv[1]
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

# Read DNA sequence
sequence_file = sys.argv[2]
with open(sequence_file, 'r') as file:
    dna_sequence = file.read()

# Compute longest run of consecutive repeats for each STR
def find_longest_run(sequence, str):
    max_count = 0
    current_count = 0
    str_len = len(str)
    for i in range(len(sequence)):
        if sequence[i:i+str_len] == str:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0
    return max_count

# Match DNA sequence with individuals in CSV file
for row in data:
    name = row['name']
    str_counts = {key: int(value) for key, value in row.items() if key != 'name'}
    match = True
    for str_name, str_count in str_counts.items():
        if find_longest_run(dna_sequence, str_name) != str_count:
            match = False
            break
    if match:
        print(name)
        sys.exit()

print("No match")