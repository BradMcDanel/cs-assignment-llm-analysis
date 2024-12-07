import csv
import sys

def read_csv(file_name):
    data = []
    with open(file_name, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)
        for row in csvreader:
            data.append({header: int(value) for header, value in zip(headers[1:], row[1:])})
    return headers[1:], data

def read_dna_sequence(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def find_match(csv_file, dna_sequence):
    headers, data = read_csv(csv_file)
    sequence = read_dna_sequence(dna_sequence)
    
    for person in data:
        match = True
        for header in headers:
            str_count = sequence.count(header * person[header])
            if str_count != person[header]:
                match = False
                break
        if match:
            print(person['name'])
            return

    print("No match")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
    else:
        csv_file = sys.argv[1]
        dna_sequence = sys.argv[2]
        find_match(csv_file, dna_sequence)