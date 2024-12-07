import csv
import sys

def read_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def read_sequence(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

def longest_match(sequence, subsequence):
    longest_run = 0
    subseq_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        count = 0
        while True:
            start = i + count * subseq_len
            end = start + subseq_len
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        longest_run = max(longest_run, count)

    return longest_run

def find_match(database, sequence):
    for person in database:
        matches = True
        for str_key in person.keys():
            if str_key == 'name':
                continue
            count = longest_match(sequence, str_key)
            if count != int(person[str_key]):
                matches = False
                break
        if matches:
            return person['name']
    return "No match"

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return

    csv_filename = sys.argv[1]
    sequence_filename = sys.argv[2]

    database = read_csv(csv_filename)
    dna_sequence = read_sequence(sequence_filename)

    match = find_match(database, dna_sequence)
    print(match)

if __name__ == "__main__":
    main()