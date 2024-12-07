import csv

def read_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

def read_dna_sequence(filename):
    with open(filename, 'r') as file:
        sequence = file.read().strip()
    return sequence

def longest_match(sequence, subsequence):
    """Returns the longest run of subsequence in sequence."""
    longest_run = 0
    sub_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        count = 0
        while sequence[i + count * sub_len : i + (count + 1) * sub_len] == subsequence:
            count += 1
        longest_run = max(longest_run, count)

    return longest_run