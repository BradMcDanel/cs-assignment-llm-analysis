import csv
import sys

def read_csv(file_path):
    # Reads the CSV file and returns the headers and data
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        data = list(reader)
    return headers, data

def read_dna_sequence(file_path):
    # Reads the DNA sequence from the text file
    with open(file_path, mode='r') as file:
        return file.read().strip()

def longest_match(sequence, subsequence):
    # Computes the longest run of consecutive repeats of subsequence in sequence
    longest_run = 0
    subseq_length = len(subsequence)
    seq_length = len(sequence)

    for i in range(seq_length):
        count = 0
        while True:
            start = i + count * subseq_length
            end = start + subseq_length
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        longest_run = max(longest_run, count)
    
    return longest_run

def find_matching_individual(database, str_counts, str_headers):
    # Finds the individual in the database whose STR counts match the given str_counts
    for person in database:
        match = all(int(person[str_header]) == str_count for str_header, str_count in zip(str_headers, str_counts))
        if match:
            return person['name']
    return "No match"

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return
    
    csv_file = sys.argv[1]
    dna_file = sys.argv[2]
    
    str_headers, database = read_csv(csv_file)
    dna_sequence = read_dna_sequence(dna_file)
    
    # Exclude the 'name' field from the STR headers
    str_headers = str_headers[1:]
    
    # Calculate the longest match for each STR in the DNA sequence
    str_counts = [longest_match(dna_sequence, str_header) for str_header in str_headers]
    
    # Find the matching individual
    matching_individual = find_matching_individual(database, str_counts, str_headers)
    print(matching_individual)

if __name__ == "__main__":
    main()