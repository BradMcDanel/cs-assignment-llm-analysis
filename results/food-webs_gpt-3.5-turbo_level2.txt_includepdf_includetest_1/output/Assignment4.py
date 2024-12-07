import sys
from formatList import formatList

def read_food_web_data(file_name):
    # Read the predator-prey relationships from the file and store them in a dictionary
    food_web_data = {}
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            predator = parts[0]
            prey_list = parts[1:]
            food_web_data[predator] = prey_list
    return food_web_data

def part1_predators_and_prey(file_name):
    # Load food web data
    food_web_data = read_food_web_data(file_name)
    
    # Display predators and their prey
    print("Predators and Prey:")
    for predator, prey_list in sorted(food_web_data.items()):
        formatted_prey = formatList(prey_list)
        print(f"  {predator} eats {formatted_prey}")

def part2_identify_apex_predators(food_web_data):
    # Identify apex predators
    apex_predators = [predator for predator in food_web_data if predator not in set(sum(food_web_data.values(), []))]
    
    # Display apex predators
    print("Apex Predators:", formatList(apex_predators))

# Implement rest of the parts (3-6) as separate functions following a similar structure

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Assignment4.py <food_web_file>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    part1_predators_and_prey(file_name)
    food_web_data = read_food_web_data(file_name)
    part2_identify_apex_predators(food_web_data)
    # Call other parts as needed