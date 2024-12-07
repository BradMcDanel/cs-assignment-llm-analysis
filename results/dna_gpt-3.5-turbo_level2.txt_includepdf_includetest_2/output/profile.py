import csv
import sys

def read_csv_file(file):
    data = []
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)
        for row in csv_reader:
            data.append(row)
    return headers, data

def read_dna_sequence(file):
    with open(file, 'r') as dna_file:
        dna_sequence = dna_file.read().replace('\n', '')
    return dna_sequence

def find_longest_str(sequence, str):
    longest_run = 0
    current_run = 0
    str_len = len(str)
    for i in range(len(sequence) - str_len):
        if sequence[i:i+str_len] == str:
            current_run += 1
            if current_run > longest_run:
                longest_run = current_run
        else:
            current_run = 0
    return longest_run

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    csv_file = sys.argv[1]
    dna_file = sys.argv[2]

    headers, data = read_csv_file(csv_file)
    dna_sequence = read_dna_sequence(dna_file)

    for i in range(1, len(headers)):
        str = headers[i]
        longest_run = find_longest_str(dna_sequence, str)
        for row in data:
            if int(row[i]) == longest_run:
                print(row[0])
                return

    print("No match")

if __name__ == "__main__":
    main()