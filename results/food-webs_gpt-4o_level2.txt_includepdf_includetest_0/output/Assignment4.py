import sys
import os

# Importing the provided formatting function
from formatList import formatList

def load_food_web(filename):
    """Load the food web from the specified file and return it as a dictionary."""
    food_web = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                food_web[predator] = prey
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    return food_web

def print_predators_and_prey(food_web):
    """Print the list of predators and their prey."""
    print("Predators and Prey:")
    for predator, prey_list in sorted(food_web.items()):
        print(f"  {predator} eats {formatList(prey_list)}")

def find_apex_predators(food_web):
    """Find and print the apex predators."""
    all_prey = {prey for prey_list in food_web.values() for prey in prey_list}
    apex_predators = [predator for predator in food_web if predator not in all_prey]
    print(f"Apex Predators: {formatList(apex_predators)}")

def find_producers(food_web):
    """Find and print the producers."""
    producers = [predator for predator, prey_list in food_web.items() if not prey_list]
    print(f"Producers: {formatList(producers)}")

def find_most_flexible_eaters(food_web):
    """Find and print the most flexible eaters."""
    max_prey_count = max(len(prey_list) for prey_list in food_web.values())
    most_flexible_eaters = [predator for predator, prey_list in food_web.items() if len(prey_list) == max_prey_count]
    print(f"Most Flexible Eaters: {formatList(most_flexible_eaters)}")

def find_tastiest_organisms(food_web):
    """Find and print the tastiest organisms."""
    prey_counts = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            prey_counts[prey] = prey_counts.get(prey, 0) + 1
    max_eaten_count = max(prey_counts.values())
    tastiest = [organism for organism, count in prey_counts.items() if count == max_eaten_count]
    print(f"Tastiest: {formatList(tastiest)}")

def determine_heights(food_web):
    """Determine and print the height of each organism in the food web."""
    heights = {organism: 0 for organism in food_web}  # Initialize all heights to 0
    changed = True
    while changed:
        changed = False
        for predator, prey_list in food_web.items():
            for prey in prey_list:
                if heights[predator] <= heights.get(prey, 0):
                    heights[predator] = heights.get(prey, 0) + 1
                    changed = True
    print("Heights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

def main():
    # Determine the file to load
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    elif len(sys.argv) > 2:
        print("Error: Too many command line arguments provided.")
        sys.exit(1)
    else:
        filename = input("Enter the file name: ")

    food_web = load_food_web(filename)
    print_predators_and_prey(food_web)
    find_apex_predators(food_web)
    find_producers(food_web)
    find_most_flexible_eaters(food_web)
    find_tastiest_organisms(food_web)
    determine_heights(food_web)

if __name__ == "__main__":
    main()