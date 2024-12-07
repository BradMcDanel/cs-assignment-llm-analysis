import sys
import os

def load_food_web(filename):
    """
    Load the food web data from a CSV file into a dictionary.
    :param filename: The name of the file to load.
    :return: A dictionary where keys are predators and values are lists of prey.
    """
    food_web = {}
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                food_web[predator] = prey
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)
    
    return food_web

def format_predator_prey(predator, prey_list):
    """
    Format the predator-prey relationship for output.
    :param predator: The predator name.
    :param prey_list: The list of prey names.
    :return: A formatted string.
    """
    if len(prey_list) == 1:
        return f"{predator} eats {prey_list[0]}"
    else:
        return f"{predator} eats {', '.join(prey_list[:-1])} and {prey_list[-1]}"

def find_apex_predators(food_web):
    """
    Identify apex predators in the food web.
    :param food_web: The dictionary of the food web.
    :return: A list of apex predators.
    """
    all_prey = {prey for prey_list in food_web.values() for prey in prey_list}
    apex_predators = [predator for predator in food_web.keys() if predator not in all_prey]
    return apex_predators

def find_producers(food_web):
    """
    Identify producers in the food web.
    :param food_web: The dictionary of the food web.
    :return: A list of producers.
    """
    producers = [organism for organism in food_web.keys() if not food_web[organism]]
    return producers

def find_most_flexible_eaters(food_web):
    """
    Identify the most flexible eaters in the food web.
    :param food_web: The dictionary of the food web.
    :return: A list of most flexible eaters.
    """
    max_prey_count = max(len(prey) for prey in food_web.values())
    flexible_eaters = [predator for predator, prey in food_web.items() if len(prey) == max_prey_count]
    return flexible_eaters

def find_tastiest_organisms(food_web):
    """
    Identify the tastiest organisms in the food web.
    :param food_web: The dictionary of the food web.
    :return: A list of tastiest organisms.
    """
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            if prey in prey_count:
                prey_count[prey] += 1
            else:
                prey_count[prey] = 1
    max_eaten_count = max(prey_count.values())
    tastiest_organisms = [organism for organism, count in prey_count.items() if count == max_eaten_count]
    return tastiest_organisms

def calculate_heights(food_web):
    """
    Calculate the heights of each organism in the food web.
    :param food_web: The dictionary of the food web.
    :return: A dictionary with organism heights.
    """
    heights = {organism: 0 for organism in food_web.keys()}
    changed = True
    
    while changed:
        changed = False
        for predator, prey_list in food_web.items():
            for prey in prey_list:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    
    return heights

def main():
    # Handle command-line arguments
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    elif len(sys.argv) == 1:
        filename = input("Please enter the name of the food web file: ")
    else:
        print("Error: Too many command-line arguments.")
        sys.exit(1)

    # Load the food web data
    food_web = load_food_web(filename)
    
    # Print the predator-prey relationships
    print("Predators and Prey:")
    for predator, prey in sorted(food_web.items()):
        print(f"  {format_predator_prey(predator, prey)}")
    
    # Identify and print apex predators
    apex_predators = find_apex_predators(food_web)
    print(f"\nApex Predators: {', '.join(sorted(apex_predators))}")

    # Identify and print producers
    producers = find_producers(food_web)
    print(f"\nProducers: {', '.join(sorted(producers))}")
    
    # Identify and print most flexible eaters
    flexible_eaters = find_most_flexible_eaters(food_web)
    print(f"\nMost Flexible Eaters: {', '.join(sorted(flexible_eaters))}")
    
    # Identify and print tastiest organisms
    tastiest_organisms = find_tastiest_organisms(food_web)
    print(f"\nTastiest: {', '.join(sorted(tastiest_organisms))}")
    
    # Calculate and print heights
    heights = calculate_heights(food_web)
    print("\nHeights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

if __name__ == "__main__":
    main()