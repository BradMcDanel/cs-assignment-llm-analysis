import sys
from formatList import formatList

def read_food_web(file_name):
    """Read the food web data from the file and return a dictionary."""
    food_web = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                food_web[predator] = prey
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        sys.exit(1)
    return food_web

def list_predators_and_prey(food_web):
    """List all predators and their prey with nice formatting."""
    print("Predators and Prey:")
    for predator in sorted(food_web.keys()):
        prey_list = formatList(food_web[predator])
        print(f"  {predator} eats {prey_list}")

def find_apex_predators(food_web):
    """Find and return a list of apex predators."""
    all_prey = set(prey for preys in food_web.values() for prey in preys)
    apex_predators = [predator for predator in food_web if predator not in all_prey]
    return apex_predators

def find_producers(food_web):
    """Find and return a list of producers."""
    producers = [organism for organism in food_web if not food_web[organism]]
    return producers

def find_most_flexible_eaters(food_web):
    """Find and return the most flexible eaters."""
    max_prey_count = max(len(prey) for prey in food_web.values())
    most_flexible_eaters = [predator for predator, prey in food_web.items() if len(prey) == max_prey_count]
    return most_flexible_eaters

def find_tastiest_organisms(food_web):
    """Find and return the tastiest organisms."""
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            if prey in prey_count:
                prey_count[prey] += 1
            else:
                prey_count[prey] = 1
    max_prey_count = max(prey_count.values())
    tastiest_organisms = [organism for organism, count in prey_count.items() if count == max_prey_count]
    return tastiest_organisms

def calculate_heights(food_web):
    """Calculate and return the heights of all organisms."""
    heights = {organism: 0 for organism in food_web}
    changed = True
    while changed:
        changed = False
        for predator, preys in food_web.items():
            for prey in preys:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    return heights

def main():
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    elif len(sys.argv) == 1:
        file_name = input("Enter the name of the food web file: ")
    else:
        print("Error: Too many command line arguments provided.")
        sys.exit(1)

    food_web = read_food_web(file_name)
    
    list_predators_and_prey(food_web)

    apex_predators = find_apex_predators(food_web)
    print(f"Apex Predators: {formatList(apex_predators)}")

    producers = find_producers(food_web)
    print(f"Producers: {formatList(producers)}")

    most_flexible_eaters = find_most_flexible_eaters(food_web)
    print(f"Most Flexible Eaters: {formatList(most_flexible_eaters)}")

    tastiest_organisms = find_tastiest_organisms(food_web)
    print(f"Tastiest: {formatList(tastiest_organisms)}")

    heights = calculate_heights(food_web)
    print("Heights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

if __name__ == "__main__":
    main()