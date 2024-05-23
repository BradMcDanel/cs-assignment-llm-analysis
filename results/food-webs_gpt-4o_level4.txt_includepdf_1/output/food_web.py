import sys
import os
from formatList import formatList

def read_food_web(file_path):
    """
    Reads the food web from a CSV file and returns a dictionary where
    keys are predators and values are lists of prey.
    """
    food_web = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                food_web[predator] = prey
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    return food_web

def display_predators_and_prey(food_web):
    """
    Displays all predators and their respective prey.
    """
    print("Predators and Prey:")
    for predator, prey in sorted(food_web.items()):
        print(f"  {predator} eats {formatList(prey)}")

def identify_apex_predators(food_web):
    """
    Identifies and returns a list of apex predators.
    """
    all_prey = {item for sublist in food_web.values() for item in sublist}
    apex_predators = [predator for predator in food_web if predator not in all_prey]
    return apex_predators

def identify_producers(food_web):
    """
    Identifies and returns a list of producers.
    """
    producers = [animal for animal, prey in food_web.items() if len(prey) == 0]
    return producers

def identify_most_flexible_eaters(food_web):
    """
    Identifies and returns a list of organisms that eat the greatest number of other organisms.
    """
    max_prey_count = max(len(prey) for prey in food_web.values())
    most_flexible_eaters = [predator for predator, prey in food_web.items() if len(prey) == max_prey_count]
    return most_flexible_eaters

def identify_tastiest_organisms(food_web):
    """
    Identifies and returns a list of organisms that are eaten by the most different members of the food chain.
    """
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            if prey not in prey_count:
                prey_count[prey] = 0
            prey_count[prey] += 1
    max_preyed_count = max(prey_count.values())
    tastiest_organisms = [organism for organism, count in prey_count.items() if count == max_preyed_count]
    return tastiest_organisms

def determine_heights(food_web):
    """
    Determines and returns a dictionary where keys are organisms and values are their heights in the food web.
    """
    heights = {organism: 0 for organism in food_web}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in food_web.items():
            for prey in prey_list:
                if heights[predator] <= heights.get(prey, 0):
                    heights[predator] = heights.get(prey, 0) + 1
                    changed = True
    return heights

def main():
    # Check command line arguments
    if len(sys.argv) > 2:
        print("Error: Too many arguments provided.")
        sys.exit(1)
    elif len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        file_path = input("Enter the name of the food web file: ")

    # Read the food web from the file
    food_web = read_food_web(file_path)

    # Display predators and prey
    display_predators_and_prey(food_web)

    # Identify and display apex predators
    apex_predators = identify_apex_predators(food_web)
    print(f"Apex Predators: {formatList(apex_predators)}")

    # Identify and display producers
    producers = identify_producers(food_web)
    print(f"Producers: {formatList(producers)}")

    # Identify and display the most flexible eaters
    most_flexible_eaters = identify_most_flexible_eaters(food_web)
    print(f"Most Flexible Eaters: {formatList(most_flexible_eaters)}")

    # Identify and display the tastiest organisms
    tastiest_organisms = identify_tastiest_organisms(food_web)
    print(f"Tastiest: {formatList(tastiest_organisms)}")

    # Determine and display the heights of each organism
    heights = determine_heights(food_web)
    print("Heights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

if __name__ == "__main__":
    main()