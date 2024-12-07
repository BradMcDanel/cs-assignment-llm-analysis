import csv
import sys

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    longest_run = 0
    subseq_length = len(subsequence)
    seq_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(seq_length):
        # Initialize count of consecutive runs
        count = 0
        # Check for a match in a substring within sequence
        while True:
            # Adjust substring start and end
            start = i + count * subseq_length
            end = start + subseq_length

            # If there's a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    return longest_run

def main():
    # Check for proper usage
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return

    # Read the DNA database file into memory
    database_filename = sys.argv[1]
    with open(database_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        individuals = list(reader)

    # Read the DNA sequence file into memory
    sequence_filename = sys.argv[2]
    with open(sequence_filename) as file:
        sequence = file.read().strip()

    # Get the list of STRs from the database
    str_names = reader.fieldnames[1:]

    # Find longest match of each STR in the sequence
    str_counts = {str_name: longest_match(sequence, str_name) for str_name in str_names}

    # Check database for matching profiles
    for person in individuals:
        if all(str_counts[str_name] == int(person[str_name]) for str_name in str_names):
            print(person['name'])
            return

    print("No match")

if __name__ == "__main__":
    main()