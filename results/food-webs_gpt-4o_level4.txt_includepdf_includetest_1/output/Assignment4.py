import sys
import os
from formatList import formatList

def load_food_web(file_path):
    """ Load predator-prey relationships from the file into a dictionary. """
    relationships = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0].strip()
                prey_list = [prey.strip() for prey in parts[1:]]
                relationships[predator] = prey_list
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    return relationships

def print_predator_prey(relationships):
    """ Print what each predator eats. """
    print("Predators and Prey:")
    for predator in sorted(relationships):
        prey_list = relationships[predator]
        print(f"  {predator} eats {formatList(prey_list)}")

def find_apex_predators(relationships):
    """ Identify and print the apex predators. """
    all_prey = {prey for preys in relationships.values() for prey in preys}
    apex_predators = [predator for predator in relationships if predator not in all_prey]
    print(f"Apex Predators: {formatList(apex_predators)}")

def find_producers(relationships):
    """ Identify and print the producers. """
    producers = [predator for predator, prey_list in relationships.items() if not prey_list]
    print(f"Producers: {formatList(producers)}")

def find_most_flexible_eaters(relationships):
    """ Identify and print the most flexible eaters. """
    max_variety = max(len(prey_list) for prey_list in relationships.values())
    flexible_eaters = [predator for predator, prey_list in relationships.items() if len(prey_list) == max_variety]
    print(f"Most Flexible Eaters: {formatList(flexible_eaters)}")

def find_tastiest_organism(relationships):
    """ Identify and print the tastiest organism. """
    prey_count = {}
    for prey_list in relationships.values():
        for prey in prey_list:
            if prey not in prey_count:
                prey_count[prey] = 0
            prey_count[prey] += 1
    max_count = max(prey_count.values())
    tastiest = [prey for prey, count in prey_count.items() if count == max_count]
    print(f"Tastiest: {formatList(tastiest)}")

def calculate_heights(relationships):
    """ Calculate and print the height of each organism. """
    heights = {organism: 0 for organism in relationships}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in relationships.items():
            for prey in prey_list:
                if prey in heights and heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    print("Heights:")
    for organism in sorted(heights):
        print(f"  {organism}: {heights[organism]}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python Assignment4.py <filename>")
        sys.exit(1)

    file_path = sys.argv[1]
    relationships = load_food_web(file_path)
    
    print_predator_prey(relationships)
    find_apex_predators(relationships)
    find_producers(relationships)
    find_most_flexible_eaters(relationships)
    find_tastiest_organism(relationships)
    calculate_heights(relationships)

if __name__ == "__main__":
    main()