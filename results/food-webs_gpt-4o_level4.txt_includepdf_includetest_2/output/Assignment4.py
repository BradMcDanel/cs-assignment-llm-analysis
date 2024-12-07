import sys
from formatList import formatList

def load_food_web(filename):
    """Load the food web data from a CSV file into a dictionary."""
    food_web = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                preys = parts[1:]
                food_web[predator] = preys
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)
    return food_web

def print_predators_and_prey(food_web):
    """Print each predator and its list of prey."""
    print("Predators and Prey:")
    for predator, preys in sorted(food_web.items()):
        print(f"  {predator} eats {formatList(preys)}")

def find_apex_predators(food_web):
    """Find and print apex predators."""
    all_preys = {prey for preys in food_web.values() for prey in preys}
    apex_predators = [predator for predator in food_web.keys() if predator not in all_preys]
    print("Apex Predators:", formatList(apex_predators))

def find_producers(food_web):
    """Find and print producers."""
    producers = [species for species, preys in food_web.items() if not preys]
    print("Producers:", formatList(producers))

def find_most_flexible_eaters(food_web):
    """Find and print the most flexible eaters."""
    max_prey_count = max(len(preys) for preys in food_web.values())
    most_flexible = [predator for predator, preys in food_web.items() if len(preys) == max_prey_count]
    print("Most Flexible Eaters:", formatList(most_flexible))

def find_tastiest_organisms(food_web):
    """Find and print the tastiest organisms."""
    prey_count = {}
    for preys in food_web.values():
        for prey in preys:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values())
    tastiest = [prey for prey, count in prey_count.items() if count == max_count]
    print("Tastiest:", formatList(tastiest))

def calculate_heights(food_web):
    """Calculate and print the height of each organism in the food web."""
    heights = {species: 0 for species in food_web}
    changed = True
    while changed:
        changed = False
        for predator, preys in food_web.items():
            for prey in preys:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    print("Heights:")
    for species, height in sorted(heights.items()):
        print(f"  {species}: {height}")

def main():
    if len(sys.argv) < 2:
        filename = input("Enter the food web filename: ")
    elif len(sys.argv) > 2:
        print("Error: Too many command line arguments provided.")
        sys.exit(1)
    else:
        filename = sys.argv[1]

    food_web = load_food_web(filename)
    print_predators_and_prey(food_web)
    find_apex_predators(food_web)
    find_producers(food_web)
    find_most_flexible_eaters(food_web)
    find_tastiest_organisms(food_web)
    calculate_heights(food_web)

if __name__ == "__main__":
    main()