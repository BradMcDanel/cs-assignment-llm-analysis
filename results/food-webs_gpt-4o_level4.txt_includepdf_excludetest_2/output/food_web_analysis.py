import sys
import os
from formatList import formatList

def load_food_web(filename):
    """Load the predator-prey relationships from a CSV file into a dictionary."""
    food_web = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    predator = parts[0]
                    prey = parts[1:]
                    food_web[predator] = prey
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)
    return food_web

def display_predators_and_prey(food_web):
    """Display what each predator eats."""
    print("Predators and Prey:")
    for predator in sorted(food_web.keys()):
        prey_list = food_web[predator]
        formatted_prey = formatList(prey_list)
        print(f"  {predator} eats {formatted_prey}")

def identify_apex_predators(food_web):
    """Identify and display apex predators."""
    all_prey = set(prey for prey_list in food_web.values() for prey in prey_list)
    apex_predators = sorted([predator for predator in food_web if predator not in all_prey])
    print(f"Apex Predators: {formatList(apex_predators)}")

def identify_producers(food_web):
    """Identify and display producers."""
    producers = sorted([predator for predator in food_web if not food_web[predator]])
    print(f"Producers: {formatList(producers)}")

def identify_most_flexible_eaters(food_web):
    """Identify and display the most flexible eaters."""
    max_prey_count = max(len(prey) for prey in food_web.values())
    flexible_eaters = sorted([predator for predator, prey in food_web.items() if len(prey) == max_prey_count])
    print(f"Most Flexible Eaters: {formatList(flexible_eaters)}")

def identify_tastiest_organisms(food_web):
    """Identify and display the tastiest organisms."""
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values())
    tastiest = sorted([prey for prey, count in prey_count.items() if count == max_count])
    print(f"Tastiest: {formatList(tastiest)}")

def calculate_heights(food_web):
    """Calculate and display the heights of each organism."""
    heights = {organism: 0 for organism in food_web}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in food_web.items():
            for prey in prey_list:
                if heights[predator] <= heights.get(prey, 0):
                    heights[predator] = heights.get(prey, 0) + 1
                    changed = True
    print("Heights:")
    for organism in sorted(heights.keys()):
        print(f"  {organism}: {heights[organism]}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python food_web_analysis.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)

    food_web = load_food_web(filename)
    display_predators_and_prey(food_web)
    identify_apex_predators(food_web)
    identify_producers(food_web)
    identify_most_flexible_eaters(food_web)
    identify_tastiest_organisms(food_web)
    calculate_heights(food_web)

if __name__ == "__main__":
    main()