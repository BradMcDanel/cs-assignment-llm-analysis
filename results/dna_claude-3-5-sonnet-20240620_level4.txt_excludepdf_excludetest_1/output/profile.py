import csv
import sys

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    # Read the CSV file into memory
    database = []
    str_names = []
    with open(sys.argv[1], 'r') as csvfile:
        reader = csv.reader(csvfile)
        str_names = next(reader)[1:]  # Get STR names, skip 'name' column
        for row in reader:
            database.append({
                'name': row[0],
                'str_counts': [int(count) for count in row[1:]]
            })

    # Read the DNA sequence
    with open(sys.argv[2], 'r') as sequence_file:
        sequence = sequence_file.read().strip()

    # Compute the longest run of each STR in the sequence
    str_counts = []
    for str_name in str_names:
        str_counts.append(longest_match(sequence, str_name))

    # Check for a matching profile
    for profile in database:
        if profile['str_counts'] == str_counts:
            print(profile['name'])
            return

    print("No match")

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each position in sequence for a match
    for i in range(sequence_length):
        count = 0
        while True:
            # If there's a match in the substring
            if sequence[i + count:i + count + subsequence_length] == subsequence:
                count += 1
            else:
                break
        
        # Update longest_run if necessary
        longest_run = max(longest_run, count)

    return longest_run

if __name__ == "__main__":
    main()