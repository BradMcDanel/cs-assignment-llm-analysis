import csv
import sys

def read_csv_file(filename):
    """
    Read the CSV file and return the header and data.
    """
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        header = reader.fieldnames
        data = list(reader)
    return header, data

def read_dna_sequence(filename):
    """
    Read the DNA sequence from the file and return it as a string.
    """
    with open(filename, 'r') as file:
        return file.read().strip()

def longest_match(sequence, subsequence):
    """
    Compute and return the longest run of consecutive repeats of the subsequence in the sequence.
    """
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

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return

    csv_filename = sys.argv[1]
    dna_filename = sys.argv[2]

    # Read the CSV file
    header, data = read_csv_file(csv_filename)
    
    # Read the DNA sequence file
    dna_sequence = read_dna_sequence(dna_filename)
    
    # Extract the STRs from the header
    str_sequences = header[1:]  # Skip the 'name' field
    
    # Calculate the longest match for each STR in the DNA sequence
    str_counts = {}
    for str_seq in str_sequences:
        str_counts[str_seq] = longest_match(dna_sequence, str_seq)
    
    # Compare against each individual's STR counts in the CSV data
    for person in data:
        match = True
        for str_seq in str_sequences:
            if int(person[str_seq]) != str_counts[str_seq]:
                match = False
                break
        if match:
            print(person['name'])
            return
    
    # If no match, print "No match"
    print("No match")

if __name__ == "__main__":
    main()