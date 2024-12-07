import sys
from formatList import formatList

def load_food_web(filename):
    """ Load the predator-prey relationships from a file into a dictionary. """
    food_web = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                food_web[predator] = prey
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        sys.exit(1)
    return food_web

def display_predators_and_prey(food_web):
    """ Display what each predator eats in a formatted manner. """
    print("Predators and Prey:")
    for predator in sorted(food_web):
        prey_list = food_web[predator]
        print(f"  {predator} eats {formatList(prey_list)}")

def find_apex_predators(food_web):
    """ Identify and display apex predators. """
    all_prey = {prey for preys in food_web.values() for prey in preys}
    apex_predators = [predator for predator in food_web.keys() if predator not in all_prey]
    print(f"Apex Predators: {formatList(apex_predators)}")

def find_producers(food_web):
    """ Identify and display producers. """
    producers = [predator for predator, prey in food_web.items() if not prey]
    print(f"Producers: {formatList(producers)}")

def find_most_flexible_eaters(food_web):
    """ Identify and display the most flexible eaters. """
    max_prey_count = max(len(prey) for prey in food_web.values())
    flexible_eaters = [predator for predator, prey in food_web.items() if len(prey) == max_prey_count]
    print(f"Most Flexible Eaters: {formatList(flexible_eaters)}")

def find_tastiest_organisms(food_web):
    """ Identify and display the tastiest organisms. """
    prey_count = {}
    for preys in food_web.values():
        for prey in preys:
            if prey not in prey_count:
                prey_count[prey] = 0
            prey_count[prey] += 1
    
    max_count = max(prey_count.values())
    tastiest_organisms = [prey for prey, count in prey_count.items() if count == max_count]
    print(f"Tastiest: {formatList(tastiest_organisms)}")

def determine_heights(food_web):
    """ Determine and display the height of each organism in the food web. """
    heights = {org: 0 for org in food_web.keys()}
    changed = True
    while changed:
        changed = False
        for predator, preys in food_web.items():
            for prey in preys:
                if prey in heights and heights[predator] <= heights[prey]:
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
    find_most_flexible_eaters(food_web)
    find_tastiest_organisms(food_web)
    determine_heights(food_web)

if __name__ == "__main__":
    main()