import csv
import sys

def read_csv_file(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

def read_dna_sequence(file_path):
    with open(file_path, 'r') as file:
        dna_sequence = file.read().replace('\n', '')
    return dna_sequence

def compute_str_counts(dna_sequence, individuals_data):
    str_counts = {}
    for i, str_sequence in enumerate(individuals_data[0][1:]):
        str_counts[str_sequence] = 0
        max_count = 0
        current_count = 0
        str_length = len(str_sequence)
        for j in range(len(dna_sequence)):
            if dna_sequence[j:j+str_length] == str_sequence:
                current_count += 1
                if current_count > max_count:
                    max_count = current_count
            else:
                current_count = 0
        str_counts[str_sequence] = max_count
    return str_counts

def identify_dna_owner(csv_file, dna_file):
    individuals_data = read_csv_file(csv_file)
    dna_sequence = read_dna_sequence(dna_file)
    str_counts = compute_str_counts(dna_sequence, individuals_data)

    for row in individuals_data[1:]:
        if [int(row[i]) for i in range(1, len(row))] == list(str_counts.values()):
            print(row[0])
            return

    print("No match")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
    else:
        identify_dna_owner(sys.argv[1], sys.argv[2])