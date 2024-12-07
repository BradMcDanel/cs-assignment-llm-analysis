import csv
import sys

def read_csv_file(filename):
    data = []
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def read_dna_sequence(filename):
    with open(filename, 'r') as file:
        return file.read()

def identify_dna_owner(csv_data, dna_sequence):
    str_counts = list(csv_data[0].keys())[1:]
    str_repeats = {str_key: 0 for str_key in str_counts}

    for str_key in str_counts:
        max_repeats = 0
        current_repeats = 0
        str_length = len(str_key)
        for i in range(len(dna_sequence)):
            if dna_sequence[i:i+str_length] == str_key:
                current_repeats += 1
                max_repeats = max(max_repeats, current_repeats)
            else:
                current_repeats = 0

        str_repeats[str_key] = max_repeats

    for person in csv_data[1:]:
        if all(int(person[str_key]) == str_repeats[str_key] for str_key in str_counts):
            print(person['name'])
            return

    print("No match")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    csv_filename = sys.argv[1]
    dna_filename = sys.argv[2]

    csv_data = read_csv_file(csv_filename)
    dna_sequence = read_dna_sequence(dna_filename)

    identify_dna_owner(csv_data, dna_sequence)