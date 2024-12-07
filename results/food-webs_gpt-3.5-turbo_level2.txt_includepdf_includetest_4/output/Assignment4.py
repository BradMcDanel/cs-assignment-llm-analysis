import sys
import formatList

def read_food_web(file_name):
    # Your code to read the food web file and store the relationships in a dictionary
    pass

def part1(food_web_data):
    # Your code for Part 1: Listing what each predator eats
    pass

def part2(food_web_data):
    # Your code for Part 2: Identifying apex predators
    pass

def part3(food_web_data):
    # Your code for Part 3: Identifying producers
    pass

def part4(food_web_data):
    # Your code for Part 4: Identifying most flexible eaters
    pass

def part5(food_web_data):
    # Your code for Part 5: Identifying the tastiest organism
    pass

def part6(food_web_data):
    # Your code for Part 6: Determining the height of each organism
    pass

def main():
    if len(sys.argv) != 2:
        print("Usage: python Assignment4.py <food_web_file>")
        sys.exit(1)
    
    file_name = sys.argv[1]

    try:
        food_web_data = read_food_web(file_name)

        part1(food_web_data)
        part2(food_web_data)
        part3(food_web_data)
        part4(food_web_data)
        part5(food_web_data)
        part6(food_web_data)

    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()