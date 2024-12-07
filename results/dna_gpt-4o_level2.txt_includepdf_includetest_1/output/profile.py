import csv
import sys

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)
    
    for i in range(sequence_length):
        count = 0
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length
            
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        
        longest_run = max(longest_run, count)
    
    return longest_run

def main():
    # Check for proper command-line usage
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return

    # Read the DNA database file
    with open(sys.argv[1], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        dna_database = list(reader)

    # Read the DNA sequence file
    with open(sys.argv[2], 'r') as file:
        dna_sequence = file.read().strip()

    # Get the STRs from the first row of the CSV
    strs = reader.fieldnames[1:]

    # Find the longest match of each STR in the DNA sequence
    str_counts = {str_: longest_match(dna_sequence, str_) for str_ in strs}

    # Check database for matching profiles
    for person in dna_database:
        if all(int(person[str_]) == str_counts[str_] for str_ in strs):
            print(person['name'])
            return
    
    print("No match")

if __name__ == "__main__":
    main()