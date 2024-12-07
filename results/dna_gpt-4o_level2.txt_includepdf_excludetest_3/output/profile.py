import csv
import sys

def read_csv_file(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        database = []
        for row in reader:
            database.append(row)
    return database

def read_dna_sequence(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

def longest_match(sequence, subseq):
    longest_run = 0
    subseq_len = len(subseq)
    sequence_len = len(sequence)

    for i in range(sequence_len):
        count = 0
        while sequence[i:i + subseq_len] == subseq:
            count += 1
            i += subseq_len
        longest_run = max(longest_run, count)
    
    return longest_run

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return

    csv_filename = sys.argv[1]
    dna_filename = sys.argv[2]

    # Read the CSV file and the DNA sequence
    database = read_csv_file(csv_filename)
    dna_sequence = read_dna_sequence(dna_filename)

    # Get the list of STRs from the CSV header (except the first column which is 'name')
    str_sequences = list(database[0].keys())[1:]

    # Calculate the longest match for each STR in the DNA sequence
    str_counts = {}
    for str_seq in str_sequences:
        str_counts[str_seq] = longest_match(dna_sequence, str_seq)

    # Compare against each record in the database
    for person in database:
        if all(str_counts[str_seq] == int(person[str_seq]) for str_seq in str_sequences):
            print(person['name'])
            return
    
    print("No match")

if __name__ == "__main__":
    main()