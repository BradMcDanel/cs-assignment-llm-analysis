import csv
import sys

def main():
    # Check for correct number of command line arguments
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    # Read command line arguments
    data_file = sys.argv[1]
    sequence_file = sys.argv[2]

    # Read DNA sequence file
    with open(sequence_file, 'r') as seq_file:
        sequence = seq_file.read()

    # Read CSV file containing STR counts
    with open(data_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        headers = csv_reader.fieldnames
        data = {row['name']: {header: int(row[header]) for header in headers[1:]} for row in csv_reader}

    # Identify to whom the DNA sequence belongs
    match_found = False
    for name, counts in data.items():
        is_match = all(sequence.count(STR * counts[STR]) == counts[STR] for STR in counts)
        if is_match:
            print(name)
            match_found = True
            break

    if not match_found:
        print("No match")

if __name__ == "__main__":
    main()