import csv
import sys

def find_dna_owner(csv_file, dna_file):
    # Read CSV file
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        headers = next(csv_reader)
        data = {row[headers['name']]: {key: int(value) for key, value in row.items() if key != 'name'} for row in csv_reader}

    # Read DNA sequence file
    with open(dna_file, 'r') as file:
        dna_sequence = file.read()

    # Compute the longest run of each STR in the DNA sequence
    str_counts = {key: 0 for key in data[list(data.keys())[0]].keys()}
    for key in str_counts:
        max_count = 0
        i = 0
        while i < len(dna_sequence):
            count = 0
            while dna_sequence[i:i+len(key)] == key:
                count += 1
                i += len(key)
            max_count = max(max_count, count)
            i += 1
        str_counts[key] = max_count

    # Match the STR counts with individuals in the CSV file
    for name, values in data.items():
        if values == str_counts:
            return name

    return "No match"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python dna_profile.py <csv_file> <dna_file>")
        sys.exit(1)

    csv_file = sys.argv[1]
    dna_file = sys.argv[2]

    result = find_dna_owner(csv_file, dna_file)
    print(result)