import csv
import sys

def read_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def read_dna_sequence(file_name):
    with open(file_name, 'r') as file:
        sequence = file.read().strip()
    return sequence

def find_matching_individual(csv_data, dna_sequence):
    str_counts = csv_data[0].keys()[1:]
    
    for individual in csv_data[1:]:
        match = True
        for str_count in str_counts:
            if dna_sequence.count(str_count) != int(individual[str_count]):
                match = False
                break
        if match:
            return individual['name']
    
    return "No match"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py <data.csv> <sequence.txt>")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    sequence_file = sys.argv[2]
    
    csv_data = read_csv(csv_file)
    dna_sequence = read_dna_sequence(sequence_file)
    
    match = find_matching_individual(csv_data, dna_sequence)
    print(match)