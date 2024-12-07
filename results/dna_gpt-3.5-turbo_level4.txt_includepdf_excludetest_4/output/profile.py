import csv
import sys

def longest_str_run(dna, str):
    max_count = 0
    current_count = 0

    for i in range(len(dna)):
        if dna[i:i+len(str)] == str:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    data_file = sys.argv[1]
    dna_file = sys.argv[2]

    try:
        with open(data_file, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            data = {row[0]: row[1:] for row in reader}

        with open(dna_file, 'r') as file:
            dna_sequence = file.read()

        for person, str_counts in data.items():
            match = True
            for i, str_count in enumerate(str_counts):
                if longest_str_run(dna_sequence, headers[i+1]) != int(str_count):
                    match = False
                    break
            if match:
                print(person)
                sys.exit(0)

        print("No match")

    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()