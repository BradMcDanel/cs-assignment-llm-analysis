# CPSC 217 Assignment 4
# Author: [Your Name]
# Student Number: [Your Student Number]
# Description: This program analyzes food webs, identifying predator-prey relationships, apex predators, producers, most flexible eaters, tastiest organisms, and organism heights.

import sys

def load_data(file_name):
    # Function to load data from the given file into a dictionary describing predator-prey relationships
    data = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip().split(',')
                predator = line[0]
                prey = line[1:]
                data[predator] = prey
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit()
    return data

def list_prey(data):
    # Function to list what each predator eats
    for predator, prey_list in data.items():
        formatted_prey = ', '.join(prey_list[:-1]) + ' and ' + prey_list[-1]
        print(f"{predator} eats {formatted_prey}")

def identify_apex_predators(data):
    # Function to identify apex predators
    apex_predators = [predator for predator in data.keys() if not any(predator in prey for prey in data.values())]
    print("Apex Predators:", ', '.join(apex_predators))

def identify_producers(data):
    # Function to identify producers
    producers = [predator for predator in data.keys() if not data[predator]]
    print("Producers:", ', '.join(producers))

def identify_most_flexible_eaters(data):
    # Function to identify the most flexible eaters
    max_eaten = max(len(prey_list) for prey_list in data.values())
    most_flexible_eaters = [predator for predator, prey_list in data.items() if len(prey_list) == max_eaten]
    print("Most Flexible Eaters:", ', '.join(most_flexible_eaters))

def identify_tastiest_organisms(data):
    # Function to identify the tastiest organisms
    prey_counts = {}
    for prey_list in data.values():
        for prey in prey_list:
            prey_counts[prey] = prey_counts.get(prey, 0) + 1
    max_count = max(prey_counts.values())
    tastiest_organsims = [organism for organism, count in prey_counts.items() if count == max_count]
    print("Tastiest Organisms:", ', '.join(tastiest_organsims))

def determine_heights(data):
    # Function to determine the height of each organism in the food web
    heights = {organism: 0 for organism in data.keys()}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in data.items():
            for prey in prey_list:
                if heights[predator] <= heights.get(prey, -1):
                    heights[predator] = heights[prey] + 1
                    changed = True
    for organism, height in heights.items():
        print(f"{organism}: {height}")

def main():
    if len(sys.argv) < 2:
        file_name = input("Enter the name of the food web file: ")
    elif len(sys.argv) > 2:
        print("Error: Too many command line arguments.")
        sys.exit()
    else:
        file_name = sys.argv[1]

    data = load_data(file_name)

    print("Predators and Prey:")
    list_prey(data)
    print()

    identify_apex_predators(data)
    print()

    identify_producers(data)
    print()

    identify_most_flexible_eaters(data)
    print()

    identify_tastiest_organisms(data)
    print()

    print("Heights:")
    determine_heights(data)

if __name__ == "__main__":
    main()