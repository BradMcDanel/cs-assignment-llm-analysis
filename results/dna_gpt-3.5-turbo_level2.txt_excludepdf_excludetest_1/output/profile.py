import csv
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    database_file = sys.argv[1]
    sequence_file = sys.argv[2]

    # Read the CSV file
    with open(database_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dna_data = row

    # Read the DNA sequence file
    with open(sequence_file, 'r') as seqfile:
        dna_sequence = seqfile.read()

    # Compute the longest run of consecutive repeats of each STR in the DNA sequence
    longest_runs = {}
    for key in dna_data.keys():
        if key != 'name':
            longest_run = 0
            current_run = 0
            str_len = len(key)
            for i in range(len(dna_sequence)):
                if dna_sequence[i:i+str_len] == key:
                    current_run += 1
                    i += str_len
                else:
                    current_run = 0
                longest_run = max(longest_run, current_run)
            longest_runs[key] = longest_run

    # Check for a matching individual
    for name, counts in dna_data.items():
        if name != 'name':
            match = True
            for key, value in counts.items():
                if longest_runs[key] != int(value):
                    match = False
                    break
            if match:
                print(name)
                return

    print("No match")

if __name__ == "__main__":
    main()