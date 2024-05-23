import csv
import sys

def load_csv_data(filename):
    """Loads the CSV data from the file and returns a list of dictionaries."""
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def load_dna_sequence(filename):
    """Loads the DNA sequence from the file and returns it as a string."""
    with open(filename, mode='r') as file:
        sequence = file.read().strip()
    return sequence

def longest_str_repeats(sequence, str_seq):
    """Computes the longest run of consecutive repeats of str_seq in the DNA sequence."""
    max_repeats = 0
    l = len(str_seq)

    for i in range(len(sequence)):
        # Count the number of consecutive repeats of str_seq starting at position i
        count = 0
        while sequence[i:i+l] == str_seq:
            count += 1
            i += l
        # Update max_repeats if the current count is greater
        max_repeats = max(max_repeats, count)
        
    return max_repeats

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return

    csv_filename = sys.argv[1]
    sequence_filename = sys.argv[2]

    # Load data from files
    dna_database = load_csv_data(csv_filename)
    dna_sequence = load_dna_sequence(sequence_filename)

    # Get the list of STRs from the CSV file (excluding the 'name' column)
    str_sequences = dna_database[0].keys()
    str_sequences = [seq for seq in str_sequences if seq != 'name']

    # Calculate the longest run of each STR in the DNA sequence
    str_counts = {}
    for str_seq in str_sequences:
        str_counts[str_seq] = longest_str_repeats(dna_sequence, str_seq)

    # Compare against each person's STR counts in the database
    for person in dna_database:
        match = True
        for str_seq in str_sequences:
            if int(person[str_seq]) != str_counts[str_seq]:
                match = False
                break
        if match:
            print(person['name'])
            return

    print("No match")

if __name__ == "__main__":
    main()