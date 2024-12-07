import csv
import sys

def find_match(csv_file, dna_file):
    # Read CSV file into memory
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    # Read DNA sequence file into memory
    with open(dna_file, 'r') as file:
        dna_sequence = file.read()

    # Extract column names
    columns = data[0].keys()

    # Compute the longest run of consecutive repeats for each STR
    str_counts = {}
    for col in columns[1:]:
        str_counts[col] = 0
        current_count = 0
        str_len = len(col)
        for i in range(len(dna_sequence) - str_len):
            if dna_sequence[i:i+str_len] == col:
                current_count += 1
                str_counts[col] = max(str_counts[col], current_count)
            else:
                current_count = 0

    # Check for a match in the CSV data
    for row in data[1:]:
        match = True
        for col in columns[1:]:
            if int(row[col]) != str_counts[col]:
                match = False
                break
        if match:
            print(row['name'])
            return

    print("No match")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
    else:
        find_match(sys.argv[1], sys.argv[2])