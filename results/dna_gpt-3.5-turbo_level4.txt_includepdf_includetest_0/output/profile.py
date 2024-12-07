import csv
import sys

def read_csv(file_path):
    data = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data[row['name']] = {key: int(value) for key, value in row.items() if key != 'name'}
    return data

def read_sequence(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def compute_str_counts(sequence, str_length):
    str_counts = {}
    for i in range(len(sequence) - str_length + 1):
        substr = sequence[i:i + str_length]
        if substr not in str_counts:
            str_counts[substr] = 1
        else:
            str_counts[substr] += 1
    return max(str_counts.values())

def identify_dna_owner(csv_data, dna_sequence):
    for name, str_counts in csv_data.items():
        match = True
        for str_type, count in str_counts.items():
            if compute_str_counts(dna_sequence, len(str_type)) != count:
                match = False
                break
        if match:
            return name
    return "No match"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)
    
    data_file = sys.argv[1]
    sequence_file = sys.argv[2]

    csv_data = read_csv(data_file)
    dna_sequence = read_sequence(sequence_file)

    result = identify_dna_owner(csv_data, dna_sequence)
    print(result)