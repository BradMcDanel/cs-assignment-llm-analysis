import sys
import formatList

def read_data_file(file_name):
    # Function to read the data file and store predator-prey relationships in a dictionary
    pass

def part1(data):
    # Function to list everything each predator eats
    pass

def part2(data):
    # Function to identify apex predators
    pass

def part3(data):
    # Function to identify producers
    pass

def part4(data):
    # Function to identify most flexible eaters
    pass

def part5(data):
    # Function to identify the tastiest organism
    pass

def part6(data):
    # Function to determine the height of each organism in the food web
    pass

def main():
    if len(sys.argv) != 2:
        print("Error: Please provide the name of the food web file as a command line argument.")
        sys.exit(1)

    file_name = sys.argv[1]

    try:
        data = read_data_file(file_name)
        part1(data)
        part2(data)
        part3(data)
        part4(data)
        part5(data)
        part6(data)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()