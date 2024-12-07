import sys
import formatList

def read_food_web(file_name):
    # Read the predator-prey relationships from the file and store them in a dictionary
    food_web = {}
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            predator = parts[0]
            prey = parts[1:]
            food_web[predator] = prey
    return food_web

def part1(food_web):
    # List everything each predator eats
    for predator, prey in food_web.items():
        formatted_prey = formatList.formatList(prey)
        print(predator, "eats", formatted_prey)

def part2(food_web):
    # Identify apex predators
    apex_predators = [predator for predator in food_web if predator not in set(sum(food_web.values(), []))]
    print("Apex Predators:", formatList.formatList(apex_predators))

# Implement functions for Part 3 to 6 similarly

def main():
    if len(sys.argv) != 2:
        print("Usage: python Assignment4.py <food_web_file>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    
    try:
        food_web = read_food_web(file_name)
        part1(food_web)
        part2(food_web)
        # Call functions for other parts here
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()