import csv
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    csv_file = sys.argv[1]
    sequence_file = sys.argv[2]

    # Read the CSV file
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        headers = next(csv_reader)
        data = {row['name']: {key: int(value) for key, value in row.items() if key != 'name'} for row in csv_reader}

    # Read the DNA sequence file
    with open(sequence_file, 'r') as file:
        sequence = file.read()

    # Compute the longest run of consecutive repeats for each STR
    str_counts = {}
    for key in headers.keys():
        if key != 'name':
            str_counts[key] = compute_longest_run(sequence, key)

    # Identify the matching individual
    for name, values in data.items():
        if values == str_counts:
            print(name)
            return

    print("No match")

def compute_longest_run(sequence, str_sequence):
    max_count = 0
    current_count = 0
    str_len = len(str_sequence)

    for i in range(len(sequence)):
        if sequence[i:i + str_len] == str_sequence:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0

    return max_count

if __name__ == "__main__":
    main()