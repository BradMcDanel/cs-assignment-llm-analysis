import sys
from collections import defaultdict

def read_food_web(file_name):
    """Reads the predator-prey relationships from a file."""
    try:
        with open(file_name, 'r') as f:
            data = f.readlines()
    except FileNotFoundError:
        print("Error: The file does not exist.")
        sys.exit()
    
    food_web = defaultdict(list)
    for line in data:
        parts = line.strip().split(',')
        predator = parts[0]
        preys = parts[1:]
        food_web[predator].extend(preys)
    
    return food_web

def display_predator_prey_relationships(food_web):
    """Displays what each predator eats."""
    print("Predators and Prey:")
    for predator, preys in sorted(food_web.items()):
        print(f"  {predator} eats {', '.join(preys[:-1])} and {preys[-1]}")

def find_apex_predators(food_web):
    """Identifies the apex predators."""
    all_prey = {prey for preys in food_web.values() for prey in preys}
    apex_predators = [predator for predator in food_web if predator not in all_prey]
    print("Apex Predators:", ', '.join(apex_predators))

def find_producers(food_web):
    """Identifies the producers."""
    producers = [organism for organism, preys in food_web.items() if not preys]
    print("Producers:", ' and '.join(producers))

def find_most_flexible_eaters(food_web):
    """Identifies the most flexible eaters."""
    max_eaten = max(len(preys) for preys in food_web.values())
    flexible_eaters = [predator for predator, preys in food_web.items() if len(preys) == max_eaten]
    print("Most Flexible Eaters:", ', '.join(flexible_eaters))

def find_tastiest_organisms(food_web):
    """Identifies the tastiest organisms."""
    prey_count = defaultdict(int)
    for preys in food_web.values():
        for prey in preys:
            prey_count[prey] += 1
    max_count = max(prey_count.values(), default=0)
    tastiest = [prey for prey in prey_count if prey_count[prey] == max_count]
    print("Tastiest:", ' and '.join(tastiest))

def determine_heights(food_web):
    """Determines the height of each organism in the food web."""
    heights = defaultdict(int)
    changed = True
    while changed:
        changed = False
        for predator, preys in food_web.items():
            for prey in preys:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    print("Heights:")
    for organism in sorted(heights.keys()):
        print(f"  {organism}: {heights[organism]}")

def main():
    if len(sys.argv) > 2:
        print("Error: Too many command line arguments.")
        sys.exit()
    elif len(sys.argv) == 1:
        file_name = input("Enter the name of the food web file: ")
    else:
        file_name = sys.argv[1]

    food_web = read_food_web(file_name)
    display_predator_prey_relationships(food_web)
    find_apex_predators(food_web)
    find_producers(food_web)
    find_most_flexible_eaters(food_web)
    find_tastiest_organisms(food_web)
    determine_heights(food_web)

if __name__ == "__main__":
    main()