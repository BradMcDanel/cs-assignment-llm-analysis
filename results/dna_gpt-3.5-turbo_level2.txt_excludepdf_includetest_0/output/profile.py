import csv
import sys

# Read CSV file
def read_csv(file_name):
    data = {}
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        for row in csv_reader:
            data[row[0]] = {headers[i]: int(row[i]) for i in range(1, len(row))}
    return data

# Read DNA sequence
def read_dna(file_name):
    with open(file_name, 'r') as file:
        return file.read()

# Find longest STR repeats
def find_longest_repeat(dna_sequence, str_sequence):
    max_repeats = 0
    current_repeats = 0
    str_len = len(str_sequence)
    i = 0
    while i < len(dna_sequence):
        if dna_sequence[i:i + str_len] == str_sequence:
            current_repeats += 1
            max_repeats = max(max_repeats, current_repeats)
            i += str_len
        else:
            current_repeats = 0
            i += 1
    return max_repeats

# Main program
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    data_file = sys.argv[1]
    sequence_file = sys.argv[2]

    database = read_csv(data_file)
    dna_sequence = read_dna(sequence_file)

    for name, str_counts in database.items():
        match = True
        for str_name, str_count in str_counts.items():
            if find_longest_repeat(dna_sequence, str_name * str_count) != str_count:
                match = False
                break
        if match:
            print(name)
            sys.exit(0)

    print("No match")