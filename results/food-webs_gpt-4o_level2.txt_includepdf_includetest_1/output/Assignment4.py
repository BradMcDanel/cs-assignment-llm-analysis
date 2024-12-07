import sys
from formatList import formatList

def load_food_web(filename):
    """Load the predator-prey relationships from a file into a dictionary."""
    relationships = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                relationships[predator] = prey
        return relationships
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: An error occurred while reading the file - {e}")
        sys.exit(1)

def print_predators_and_prey(relationships):
    """Print all predators and their prey."""
    print("Predators and Prey:")
    for predator, prey in sorted(relationships.items()):
        formatted_prey = formatList(prey)
        print(f"  {predator} eats {formatted_prey}")

def find_apex_predators(relationships):
    """Find and print apex predators."""
    all_prey = {prey for preys in relationships.values() for prey in preys}
    apex_predators = [predator for predator in relationships if predator not in all_prey]
    print(f"Apex Predators: {formatList(apex_predators)}")

def find_producers(relationships):
    """Find and print producers."""
    producers = [predator for predator, prey in relationships.items() if len(prey) == 0]
    print(f"Producers: {formatList(producers)}")

def find_most_flexible_eaters(relationships):
    """Find and print the most flexible eaters."""
    max_prey_count = max(len(prey) for prey in relationships.values())
    most_flexible_eaters = [predator for predator, prey in relationships.items() if len(prey) == max_prey_count]
    print(f"Most Flexible Eaters: {formatList(most_flexible_eaters)}")

def find_tastiest_organisms(relationships):
    """Find and print the tastiest organisms."""
    prey_count = {}
    for preys in relationships.values():
        for prey in preys:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_preyed_count = max(prey_count.values())
    tastiest_organisms = [prey for prey, count in prey_count.items() if count == max_preyed_count]
    print(f"Tastiest: {formatList(tastiest_organisms)}")

def calculate_heights(relationships):
    """Calculate and print the height of each organism in the food web."""
    heights = {organism: 0 for organism in relationships}
    changed = True
    while changed:
        changed = False
        for predator, preys in relationships.items():
            for prey in preys:
                if heights[predator] <= heights.get(prey, 0):
                    heights[predator] = heights.get(prey, 0) + 1
                    changed = True
    print("Heights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python Assignment4.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    relationships = load_food_web(filename)
    
    print_predators_and_prey(relationships)
    find_apex_predators(relationships)
    find_producers(relationships)
    find_most_flexible_eaters(relationships)
    find_tastiest_organisms(relationships)
    calculate_heights(relationships)

if __name__ == "__main__":
    main()