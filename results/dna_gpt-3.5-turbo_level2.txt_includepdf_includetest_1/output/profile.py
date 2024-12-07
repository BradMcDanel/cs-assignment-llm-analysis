import csv
import sys

def read_csv(file_path):
    data = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data[row['name']] = {key: int(value) for key, value in row.items() if key != 'name'}
    return data

def read_dna_sequence(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def find_match(csv_data, dna_sequence):
    for name, str_counts in csv_data.items():
        match = True
        for str_key, str_count in str_counts.items():
            if dna_sequence.count(str_key * str_count) != str_count:
                match = False
                break
        if match:
            return name
    return "No match"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py <data.csv> <sequence.txt>")
        sys.exit(1)

    csv_file = sys.argv[1]
    dna_file = sys.argv[2]

    csv_data = read_csv(csv_file)
    dna_sequence = read_dna_sequence(dna_file)

    match = find_match(csv_data, dna_sequence)
    print(match)