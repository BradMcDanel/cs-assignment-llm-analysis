import csv
import sys

def read_csv_file(csv_file):
    data = {}
    
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        
        for row in csv_reader:
            name = row[0]
            counts = [int(count) for count in row[1:]]
            data[name] = counts
        
    return data

def read_dna_sequence(dna_file):
    with open(dna_file, 'r') as file:
        return file.read()

def find_matching_individual(csv_data, dna_sequence):
    for name, counts in csv_data.items():
        match = True
        
        for i in range(1, len(counts)):
            str_count = counts[i]
            str_sequence = header[i]
            
            if str_sequence * str_count not in dna_sequence:
                match = False
                break
        
        if match:
            return name
    
    return "No match"

if __name__ == "__main__":
    csv_file = sys.argv[1]
    dna_file = sys.argv[2]
    
    csv_data = read_csv_file(csv_file)
    dna_sequence = read_dna_sequence(dna_file)
    
    header = list(csv_data.values())[0]
    
    matching_individual = find_matching_individual(csv_data, dna_sequence)
    print(matching_individual)