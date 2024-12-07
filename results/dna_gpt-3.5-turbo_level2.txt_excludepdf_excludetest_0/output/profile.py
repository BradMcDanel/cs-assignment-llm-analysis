import csv
import sys

# Read CSV file
def read_csv(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

# Read DNA sequence file
def read_sequence(filename):
    with open(filename, 'r') as file:
        sequence = file.read()
    return sequence

# Compute longest run of consecutive repeats of the STR in the DNA sequence
def find_str(sequence, str_pattern):
    max_count = 0
    current_count = 0
    str_len = len(str_pattern)
    for i in range(len(sequence)):
        if sequence[i:i+str_len] == str_pattern:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0
    return max_count

# Main program
def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    data_filename = sys.argv[1]
    sequence_filename = sys.argv[2]

    data = read_csv(data_filename)
    sequence = read_sequence(sequence_filename)

    for row in data[1:]:
        individual = row['name']
        str_counts = {key: int(value) for key, value in row.items() if key != 'name'}
        match = True
        for str_key, str_value in str_counts.items():
            if find_str(sequence, str_key) != str_value:
                match = False
                break
        if match:
            print(individual)
            return

    print("No match")

if __name__ == "__main__":
    main()