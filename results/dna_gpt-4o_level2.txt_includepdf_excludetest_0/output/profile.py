import csv
import sys

def read_csv_file(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        str_names = reader.fieldnames[1:]  # Exclude the 'name' field
        people = list(reader)
    return str_names, people

def read_dna_sequence(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

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

def find_matching_person(str_counts, people):
    for person in people:
        match = True
        for str_name in str_counts:
            if int(person[str_name]) != str_counts[str_name]:
                match = False
                break
        if match:
            return person['name']
    return "No match"

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return

    csv_filename = sys.argv[1]
    sequence_filename = sys.argv[2]

    str_names, people = read_csv_file(csv_filename)
    sequence = read_dna_sequence(sequence_filename)

    str_counts = {str_name: longest_match(sequence, str_name) for str_name in str_names}

    match = find_matching_person(str_counts, people)
    print(match)

if __name__ == "__main__":
    main()