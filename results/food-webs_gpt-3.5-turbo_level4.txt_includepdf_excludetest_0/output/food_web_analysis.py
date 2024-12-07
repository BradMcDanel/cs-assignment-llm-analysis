import sys

def read_data_file(file_name):
    # Read the file and store the predator-prey relationships

def part1(data):
    # List everything that each predator eats on a single line with nice formatting

def part2(data):
    # Identify and display all of the apex predators

def part3(data):
    # Identify and display all of the producers

def part4(data):
    # Identify and display all of the most flexible eaters

def part5(data):
    # Identify and display the tastiest organisms

def part6(data):
    # Determine the height of each organism in the food web

def main():
    if len(sys.argv) == 1:
        file_name = input("Enter the name of the file: ")
    elif len(sys.argv) == 2:
        file_name = sys.argv[1]
    else:
        print("Error: Incorrect number of command line arguments")
        sys.exit(1)

    data = read_data_file(file_name)
    part1(data)
    part2(data)
    part3(data)
    part4(data)
    part5(data)
    part6(data)

if __name__ == "__main__":
    main()