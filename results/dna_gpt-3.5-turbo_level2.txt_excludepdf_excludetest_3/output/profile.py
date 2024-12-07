import csv
import sys

def read_csv(file):
    data = []
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def read_sequence(file):
    with open(file, 'r') as seqfile:
        sequence = seqfile.read()
    return sequence

def find_match(csv_data, dna_sequence):
    for person in csv_data:
        match = True
        for key, value in person.items():
            if key != 'name' and dna_sequence.count(value) != int(person[key]):
                match = False
                break
        if match:
            return person['name']
    return "No match"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    csv_file = sys.argv[1]
    sequence_file = sys.argv[2]

    csv_data = read_csv(csv_file)
    dna_sequence = read_sequence(sequence_file)

    match = find_match(csv_data, dna_sequence)
    print(match)