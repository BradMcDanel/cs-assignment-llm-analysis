import csv
import sys

def load_database(filename):
    """Load the DNA database from a CSV file."""
    database = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            database.append(row)
    return database, reader.fieldnames[1:]  # Return database and STR names

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

def profile_dna(database, sequence, str_names):
    """Profile the DNA sequence against the database."""
    profile = {}
    for str_name in str_names:
        profile[str_name] = longest_match(sequence, str_name)
    
    for person in database:
        if all(int(person[str_name]) == profile[str_name] for str_name in str_names):
            return person['name']
    return "No match"

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python profile.py data.csv sequence.txt")

    database_file = sys.argv[1]
    sequence_file = sys.argv[2]

    # Load database
    database, str_names = load_database(database_file)

    # Load DNA sequence
    with open(sequence_file, 'r') as f:
        sequence = f.read().strip()

    # Find matching profile
    result = profile_dna(database, sequence, str_names)
    print(result)

if __name__ == "__main__":
    main()