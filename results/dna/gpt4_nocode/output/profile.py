import csv
import sys

def main():
    # Ensure correct usage
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)
    
    csv_filename = sys.argv[1]
    sequence_filename = sys.argv[2]
    
    # Read the DNA sequence file
    with open(sequence_filename, 'r') as file:
        dna_sequence = file.read().strip()
    
    # Read the CSV file and extract STRs and profiles
    with open(csv_filename, 'r') as file:
        reader = csv.DictReader(file)
        individuals = list(reader)
        strs = reader.fieldnames[1:]  # Skipping the first fieldname which is 'name'
    
    # Compute the longest run of each STR in the DNA sequence
    str_counts = {str_: longest_run(dna_sequence, str_) for str_ in strs}
    
    # Check each individual's STR counts against the computed STR counts
    for individual in individuals:
        if all(int(individual[str_]) == str_counts[str_] for str_ in strs):
            print(individual['name'])
            break
    else:
        print("No match")

def longest_run(sequence, str_):
    """Returns the longest run of the substring str_ in the sequence."""
    max_run = 0
    length = len(str_)
    for i in range(len(sequence)):
        current_run = 0
        while sequence[i:i+length] == str_:
            current_run += 1
            i += length
        if current_run > max_run:
            max_run = current_run
    return max_run

if __name__ == "__main__":
    main()