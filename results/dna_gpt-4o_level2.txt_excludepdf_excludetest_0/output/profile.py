import csv
import sys

def read_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data, reader.fieldnames[1:]

def read_dna_sequence(filename):
    with open(filename, 'r') as file:
        sequence = file.read().strip()
    return sequence

def longest_match(sequence, subsequence):
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)
    
    for i in range(sequence_length):
        count = 0
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        longest_run = max(longest_run, count)
    
    return longest_run

def find_match(dna_data, str_counts, str_names):
    for person in dna_data:
        if all(int(person[str_seq]) == str_counts[str_seq] for str_seq in str_names):
            return person['name']
    return "No match"

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return

    csv_filename = sys.argv[1]
    dna_filename = sys.argv[2]

    dna_data, str_names = read_csv(csv_filename)
    dna_sequence = read_dna_sequence(dna_filename)

    str_counts = {str_seq: longest_match(dna_sequence, str_seq) for str_seq in str_names}

    match = find_match(dna_data, str_counts, str_names)
    print(match)

if __name__ == "__main__":
    main()