import sys

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit()

def process_data(data):
    relationships = {}
    for line in data:
        line = line.strip().split(',')
        predator = line[0]
        prey = line[1:]
        relationships[predator] = prey
    return relationships

def part_1(data):
    relationships = process_data(data)
    for predator, prey in sorted(relationships.items()):
        print(f"{predator} eats {formatList(prey)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments.")
        sys.exit()
    
    file_name = sys.argv[1]
    file_data = read_file(file_name)
    part_1(file_data)