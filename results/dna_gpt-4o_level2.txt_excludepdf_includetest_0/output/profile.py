import csv
import sys

def read_csv_file(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        individuals = list(reader)
    return individuals

def read_dna_sequence(filename):
    with open(filename, 'r') as file:
        sequence = file.read().strip()
    return sequence

def longest_match(sequence, subsequence):
    longest_run = 0
    sub_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        count = 0

        while True:
            start = i + count * sub_len
            end = start + sub_len

            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        longest_run = max(longest_run, count)

    return longest_run

def find_matching_individual(individuals, str_counts):
    for individual in individuals:
        if all(int(individual[str_name]) == str_counts[str_name] for str_name in str_counts):
            return individual['name']
    return "No match"

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return

    csv_filename = sys.argv[1]
    sequence_filename = sys.argv[2]

    individuals = read_csv_file(csv_filename)
    sequence = read_dna_sequence(sequence_filename)

    if not individuals:
        print("No individuals found in the database.")
        return

    str_names = individuals[0].keys() - {'name'}
    str_counts = {}

    for str_name in str_names:
        str_counts[str_name] = longest_match(sequence, str_name)

    matching_individual = find_matching_individual(individuals, str_counts)
    print(matching_individual)

if __name__ == "__main__":
    main()