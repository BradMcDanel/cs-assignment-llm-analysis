import csv
import sys

def longest_run(sequence, subseq):
    """Return the maximum number of times the subsequence repeats in sequence."""
    max_run = 0
    subseq_len = len(subseq)
    for i in range(len(sequence)):
        run_length = 0
        while sequence[i:i+subseq_len] == subseq:
            run_length += 1
            i += subseq_len
        if run_length > max_run:
            max_run = run_length
    return max_run

def match_dna(database, sequence):
    """Match the DNA sequence to the database entries."""
    with open(database, mode='r') as db_file:
        db_reader = csv.DictReader(db_file)
        for row in db_reader:
            match = True
            for subseq in row:
                if subseq == 'name':
                    continue
                if int(row[subseq]) != longest_run(sequence, subseq):
                    match = False
                    break
            if match:
                return row['name']
    return "No match"

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python profile.py data.csv sequence.txt")
    
    database = sys.argv[1]
    sequence_file = sys.argv[2]
    
    try:
        with open(sequence_file, mode='r') as seq_file:
            sequence = seq_file.read().strip()
    except FileNotFoundError:
        sys.exit(f"Error: {sequence_file} does not exist.")
    
    match = match_dna(database, sequence)
    print(match)

if __name__ == "__main__":
    main()