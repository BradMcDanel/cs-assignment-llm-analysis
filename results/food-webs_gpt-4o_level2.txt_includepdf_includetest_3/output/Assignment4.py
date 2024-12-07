import sys
from formatList import formatList

def load_food_web(file_name):
    """Load predator-prey relationships from a given file into a dictionary."""
    try:
        with open(file_name, 'r') as file:
            food_web = {}
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0].strip()
                prey = [p.strip() for p in parts[1:]]
                food_web[predator] = prey
            return food_web
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        sys.exit(1)

def list_predators_and_prey(food_web):
    """Outputs what each predator eats."""
    print("Predators and Prey:")
    for predator in sorted(food_web.keys()):
        prey_list = formatList(food_web[predator])
        print(f"  {predator} eats {prey_list}")

def find_apex_predators(food_web):
    """Identify apex predators."""
    all_prey = set(p for prey_list in food_web.values() for p in prey_list)
    apex_predators = sorted([predator for predator in food_web if predator not in all_prey])
    print(f"Apex Predators: {formatList(apex_predators)}")

def find_producers(food_web):
    """Identify producers."""
    producers = sorted([pred for pred, prey in food_web.items() if len(prey) == 0])
    print(f"Producers: {formatList(producers)}")

def find_most_flexible_eaters(food_web):
    """Identify the most flexible eaters."""
    max_prey_count = max(len(prey) for prey in food_web.values())
    most_flexible_eaters = sorted([predator for predator, prey in food_web.items() if len(prey) == max_prey_count])
    print(f"Most Flexible Eaters: {formatList(most_flexible_eaters)}")

def find_tastiest_organisms(food_web):
    """Identify the tastiest organisms."""
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_preyed_count = max(prey_count.values(), default=0)
    tastiest_organisms = sorted([prey for prey, count in prey_count.items() if count == max_preyed_count])
    print(f"Tastiest: {formatList(tastiest_organisms)}")

def determine_heights(food_web):
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
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    elif len(sys.argv) == 1:
        file_name = input("Please enter the name of the food web file: ")
    else:
        print("Error: Too many arguments provided. Please provide only the file name.")
        sys.exit(1)

    food_web = load_food_web(file_name)
    list_predators_and_prey(food_web)
    find_apex_predators(food_web)
    find_producers(food_web)
    find_most_flexible_eaters(food_web)
    find_tastiest_organisms(food_web)
    determine_heights(food_web)

if __name__ == "__main__":
    main()