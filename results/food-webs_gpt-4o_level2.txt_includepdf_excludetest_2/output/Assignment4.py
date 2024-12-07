# Author: [Your Name]
# Student Number: [Your Student Number]
# Description: This script analyzes food webs from a given CSV file and identifies relationships such as apex predators,
# producers, most flexible eaters, tastiest organisms, and the height of each organism in the food web.

import sys
import os
from formatList import formatList

def load_food_web(filename):
    """Load the food web from the given filename."""
    try:
        with open(filename, 'r') as file:
            food_web = {}
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0].strip()
                prey_list = [prey.strip() for prey in parts[1:]]
                food_web[predator] = prey_list
        return food_web
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
        sys.exit(1)

def display_predators_and_prey(food_web):
    """Display the predators and their respective prey in a formatted output."""
    print("Predators and Prey:")
    for predator, prey_list in sorted(food_web.items()):
        print(f"  {predator} eats {formatList(prey_list)}")

def find_apex_predators(food_web):
    """Identify and display apex predators."""
    all_prey = set(prey for preys in food_web.values() for prey in preys)
    apex_predators = [predator for predator in food_web if predator not in all_prey]
    print(f"Apex Predators: {formatList(sorted(apex_predators))}")

def find_producers(food_web):
    """Identify and display producers."""
    producers = [organism for organism, preys in food_web.items() if len(preys) == 0]
    print(f"Producers: {formatList(sorted(producers))}")

def find_flexible_eaters(food_web):
    """Identify and display the most flexible eaters."""
    max_prey_count = max(len(preys) for preys in food_web.values())
    flexible_eaters = [predator for predator, preys in food_web.items() if len(preys) == max_prey_count]
    print(f"Most Flexible Eaters: {formatList(sorted(flexible_eaters))}")

def find_tastiest_organisms(food_web):
    """Identify and display the tastiest organisms."""
    prey_count = {}
    for preys in food_web.values():
        for prey in preys:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values())
    tastiest = [prey for prey, count in prey_count.items() if count == max_count]
    print(f"Tastiest: {formatList(sorted(tastiest))}")

def calculate_heights(food_web):
    """Calculate and display the height of each organism."""
    heights = {organism: 0 for organism in food_web}

    changed = True
    while changed:
        changed = False
        for predator, preys in food_web.items():
            for prey in preys:
                if heights[predator] <= heights.get(prey, 0):
                    heights[predator] = heights[prey] + 1
                    changed = True

    print("Heights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    elif len(sys.argv) == 1:
        filename = input("Enter the name of the file: ")
    else:
        print("Error: Too many command line arguments provided.")
        sys.exit(1)

    food_web = load_food_web(filename)
    
    display_predators_and_prey(food_web)
    find_apex_predators(food_web)
    find_producers(food_web)
    find_flexible_eaters(food_web)
    find_tastiest_organisms(food_web)
    calculate_heights(food_web)

if __name__ == "__main__":
    main()