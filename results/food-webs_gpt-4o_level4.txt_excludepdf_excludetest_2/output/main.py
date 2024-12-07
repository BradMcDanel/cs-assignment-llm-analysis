import sys
import os

def read_food_web(file_path):
    """ Reads the predator-prey relationships from a CSV file and returns a dictionary. """
    food_web = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                food_web[predator] = prey
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        sys.exit(1)
    return food_web

def list_predators_and_prey(food_web):
    """ Lists each predator and its prey in a formatted manner. """
    print("Predators and Prey:")
    for predator, prey in sorted(food_web.items()):
        formatted_prey = ", ".join(prey[:-1]) + " and " + prey[-1] if len(prey) > 1 else prey[0]
        print(f"  {predator} eats {formatted_prey}")

def find_apex_predators(food_web):
    """ Identifies and prints apex predators. """
    all_prey = set(prey for prey_list in food_web.values() for prey in prey_list)
    apex_predators = [predator for predator in food_web if predator not in all_prey]
    print(f"Apex Predators: {', '.join(apex_predators)}")

def find_producers(food_web):
    """ Identifies and prints producers. """
    producers = [predator for predator, prey in food_web.items() if not prey]
    print(f"Producers: {', '.join(producers)}")

def find_most_flexible_eaters(food_web):
    """ Identifies and prints the most flexible eaters. """
    max_prey_count = max(len(prey) for prey in food_web.values())
    most_flexible_eaters = [predator for predator, prey in food_web.items() if len(prey) == max_prey_count]
    print(f"Most Flexible Eaters: {', '.join(most_flexible_eaters)}")

def find_tastiest_organism(food_web):
    """ Identifies and prints the tastiest organisms. """
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values())
    tastiest_organisms = [prey for prey, count in prey_count.items() if count == max_count]
    print(f"Tastiest: {', '.join(tastiest_organisms)}")

def determine_heights(food_web):
    """ Determines and prints the height of each organism. """
    heights = {animal: 0 for animal in food_web}  # Initialize heights
    changed = True
    while changed:
        changed = False
        for predator, prey_list in food_web.items():
            for prey in prey_list:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    print("Heights:")
    for animal, height in sorted(heights.items()):
        print(f"  {animal}: {height}")

def main():
    # Handle command line arguments
    if len(sys.argv) > 2:
        print("Error: Too many command line arguments.")
        sys.exit(1)
    elif len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        file_path = input("Enter the path to the food web file: ")

    # Read the food web data
    food_web = read_food_web(file_path)

    # Execute each part of the assignment
    list_predators_and_prey(food_web)
    find_apex_predators(food_web)
    find_producers(food_web)
    find_most_flexible_eaters(food_web)
    find_tastiest_organism(food_web)
    determine_heights(food_web)

if __name__ == "__main__":
    main()