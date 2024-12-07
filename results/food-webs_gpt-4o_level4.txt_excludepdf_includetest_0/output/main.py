import sys

def load_food_web(file_name):
    """Load the food web from a file into a dictionary."""
    food_web = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey_list = parts[1:]
                food_web[predator] = prey_list
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        sys.exit(1)
    return food_web

def display_predators_and_prey(food_web):
    """Display each predator and what it eats."""
    print("Predators and Prey:")
    for predator, prey_list in sorted(food_web.items()):
        prey_str = ", ".join(prey_list[:-1]) + " and " + prey_list[-1] if len(prey_list) > 1 else prey_list[0]
        print(f"  {predator} eats {prey_str}")

def find_apex_predators(food_web):
    """Identify and display apex predators."""
    all_prey = set(prey for preys in food_web.values() for prey in preys)
    apex_predators = [predator for predator in food_web if predator not in all_prey]
    print("Apex Predators:", ", ".join(apex_predators))

def find_producers(food_web):
    """Identify and display producers."""
    producers = [predator for predator, prey in food_web.items() if not prey]
    print("Producers:", ", ".join(producers))

def find_most_flexible_eaters(food_web):
    """Identify and display the most flexible eaters."""
    max_prey_count = max(len(prey) for prey in food_web.values())
    most_flexible_eaters = [predator for predator, prey in food_web.items() if len(prey) == max_prey_count]
    print("Most Flexible Eaters:", ", ".join(most_flexible_eaters))

def find_tastiest_organisms(food_web):
    """Identify and display the tastiest organisms."""
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values())
    tastiest_organisms = [prey for prey, count in prey_count.items() if count == max_count]
    print("Tastiest:", ", ".join(tastiest_organisms))

def calculate_heights(food_web):
    """Determine and display the height of each organism."""
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
    if len(sys.argv) != 2:
        file_name = input("Enter the name of the food web file: ")
    else:
        file_name = sys.argv[1]

    food_web = load_food_web(file_name)
    
    display_predators_and_prey(food_web)
    find_apex_predators(food_web)
    find_producers(food_web)
    find_most_flexible_eaters(food_web)
    find_tastiest_organisms(food_web)
    calculate_heights(food_web)

if __name__ == "__main__":
    main()