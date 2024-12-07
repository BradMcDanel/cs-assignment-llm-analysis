import sys
from formatList import formatList

def load_food_web(filename):
    """Load the predator-prey relations from the given file."""
    try:
        with open(filename, 'r') as f:
            food_web = {}
            for line in f:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                food_web[predator] = prey
            return food_web
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

def display_predators_and_prey(food_web):
    """Display what each predator eats."""
    print("Predators and Prey:")
    for predator, prey in sorted(food_web.items()):
        print(f"  {predator} eats {formatList(prey)}")

def find_apex_predators(food_web):
    """Identify apex predators."""
    all_prey = set(prey for preys in food_web.values() for prey in preys)
    apex_predators = [predator for predator in food_web if predator not in all_prey]
    print(f"Apex Predators: {formatList(apex_predators)}")

def find_producers(food_web):
    """Identify producers."""
    producers = [predator for predator, prey in food_web.items() if not prey]
    print(f"Producers: {formatList(producers)}")

def find_most_flexible_eaters(food_web):
    """Identify the most flexible eaters."""
    max_variety = max(len(prey) for prey in food_web.values())
    flexible_eaters = [predator for predator, prey in food_web.items() if len(prey) == max_variety]
    print(f"Most Flexible Eaters: {formatList(flexible_eaters)}")

def find_tastiest_organisms(food_web):
    """Identify the tastiest organisms."""
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            if prey not in prey_count:
                prey_count[prey] = 0
            prey_count[prey] += 1
    max_count = max(prey_count.values(), default=0)
    tastiest = [prey for prey, count in prey_count.items() if count == max_count]
    print(f"Tastiest: {formatList(tastiest)}")

def calculate_heights(food_web):
    """Determine the height of each organism in the food web."""
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
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

def main():
    # Handle command line arguments
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    elif len(sys.argv) > 2:
        print("Error: More than one command line argument provided.")
        sys.exit(1)
    else:
        filename = input("Please enter the file name: ")

    # Load the food web
    food_web = load_food_web(filename)

    # Part 1: Display predators and prey
    display_predators_and_prey(food_web)

    # Part 2: Identify apex predators
    find_apex_predators(food_web)

    # Part 3: Identify producers
    find_producers(food_web)

    # Part 4: Identify the most flexible eaters
    find_most_flexible_eaters(food_web)

    # Part 5: Identify the tastiest organisms
    find_tastiest_organisms(food_web)

    # Part 6: Calculate heights
    calculate_heights(food_web)

# Ensure the script is executable
if __name__ == "__main__":
    main()