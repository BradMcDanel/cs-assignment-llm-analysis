import csv
import sys

def read_csv_file(filename):
    """Reads the CSV file and returns the data as a list of dictionaries."""
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def read_dna_sequence(filename):
    """Reads the DNA sequence from a text file and returns it as a string."""
    with open(filename, 'r') as file:
        return file.read().strip()

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    longest_run = 0
    sub_len = len(subsequence)

    for i in range(len(sequence)):
        # Initialize count of consecutive runs
        count = 0

        # Check for consecutive matches
        while i + count * sub_len < len(sequence) and sequence[i + count * sub_len:i + (count + 1) * sub_len] == subsequence:
            count += 1

        # Update maximum run length
        longest_run = max(longest_run, count)

    return longest_run

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    csv_filename = sys.argv[1]
    sequence_filename = sys.argv[2]

    # Read the database and DNA sequence
    database = read_csv_file(csv_filename)
    dna_sequence = read_dna_sequence(sequence_filename)

    # Get the list of STRs from the database's first row (excluding the 'name' field)
    if not database:
        print("No data in CSV file.")
        sys.exit(1)

    str_names = database[0].keys() - {'name'}

    # Find longest match of each STR in the DNA sequence
    str_counts = {str_name: longest_match(dna_sequence, str_name) for str_name in str_names}

    # Check database for matching profiles
    for person in database:
        if all(int(person[str_name]) == str_counts[str_name] for str_name in str_names):
            print(person['name'])
            return

    print("No match")

if __name__ == "__main__":
    main()