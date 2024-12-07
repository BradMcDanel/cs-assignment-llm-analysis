import csv
import sys

def read_csv(file_path):
    with open(file_path) as file:
        reader = csv.DictReader(file)
        people = [row for row in reader]
    return people

def read_dna(file_path):
    with open(file_path) as file:
        dna_sequence = file.read().strip()
    return dna_sequence

def longest_consecutive_repeats(dna_sequence, str_sequence):
    max_repeats = 0
    str_len = len(str_sequence)
    for i in range(len(dna_sequence)):
        count = 0
        while dna_sequence[i:i + str_len] == str_sequence:
            count += 1
            i += str_len
        max_repeats = max(max_repeats, count)
    return max_repeats

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return

    csv_file = sys.argv[1]
    dna_file = sys.argv[2]

    people = read_csv(csv_file)
    dna_sequence = read_dna(dna_file)

    str_sequences = list(people[0].keys())[1:]  # exclude 'name' column
    str_counts = {str_sequence: longest_consecutive_repeats(dna_sequence, str_sequence) for str_sequence in str_sequences}

    for person in people:
        if all(int(person[str_sequence]) == str_counts[str_sequence] for str_sequence in str_sequences):
            print(person['name'])
            return

    print("No match")

if __name__ == "__main__":
    main()