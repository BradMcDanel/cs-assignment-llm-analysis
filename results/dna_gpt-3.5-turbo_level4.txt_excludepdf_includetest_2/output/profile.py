import csv
import sys

def identify_dna_owner(csv_file, dna_file):
    # Read the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        headers = next(reader)
        data = {row['name']: {k: int(v) for k, v in row.items() if k != 'name'} for row in reader}

    # Read the DNA sequence file
    with open(dna_file, 'r') as file:
        dna_sequence = file.read()

    # Compute the longest run of consecutive repeats for each STR
    longest_str_counts = {str_key: 0 for str_key in data[list(data.keys())[0]].keys()}
    for str_key in longest_str_counts.keys():
        str_len = len(str_key)
        max_count = 0
        current_count = 0
        for i in range(len(dna_sequence) - str_len):
            if dna_sequence[i:i+str_len] == str_key:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
        longest_str_counts[str_key] = max_count

    # Identify the DNA owner
    for name, str_counts in data.items():
        if str_counts == longest_str_counts:
            print(name)
            return

    print("No match")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    csv_file = sys.argv[1]
    dna_file = sys.argv[2]
    identify_dna_owner(csv_file, dna_file)