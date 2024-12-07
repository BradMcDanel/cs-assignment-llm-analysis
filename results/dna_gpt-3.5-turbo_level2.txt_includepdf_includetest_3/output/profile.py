import csv
import sys

def read_csv(file_path):
    data = {}
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for row in csv_reader:
            name = row[0]
            counts = [int(count) for count in row[1:]]
            data[name] = counts
    return data

def read_dna_sequence(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def compute_str_counts(sequence, str_sequence):
    max_counts = 0
    current_counts = 0
    str_length = len(str_sequence)

    for i in range(len(sequence) - str_length + 1):
        if sequence[i:i+str_length] == str_sequence:
            current_counts += 1
            max_counts = max(max_counts, current_counts)
        else:
            current_counts = 0

    return max_counts

def identify_dna_owner(csv_file, dna_file):
    str_data = read_csv(csv_file)
    dna_sequence = read_dna_sequence(dna_file)

    for name, str_counts in str_data.items():
        match = True
        for i, str_count in enumerate(str_counts):
            str_sequence = str_data['name'][i]
            if compute_str_counts(dna_sequence, str_sequence) != str_count:
                match = False
                break

        if match:
            return name

    return "No match"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py <csv_file> <dna_file>")
    else:
        csv_file = sys.argv[1]
        dna_file = sys.argv[2]
        result = identify_dna_owner(csv_file, dna_file)
        print(result)