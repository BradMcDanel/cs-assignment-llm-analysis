import sys
from formatList import formatList

def load_data(filename):
    """Load predator-prey data from a file into a dictionary."""
    try:
        with open(filename, 'r') as file:
            data = {}
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                data[predator] = prey
            return data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

def list_predators_and_prey(data):
    """List each predator and what it eats."""
    print("Predators and Prey:")
    for predator in sorted(data.keys()):
        prey_list = data[predator]
        formatted_prey = formatList(prey_list)
        print(f"  {predator} eats {formatted_prey}")

def find_apex_predators(data):
    """Identify apex predators."""
    all_prey = set()
    for prey_list in data.values():
        all_prey.update(prey_list)
    apex_predators = [predator for predator in data if predator not in all_prey]
    print(f"Apex Predators: {formatList(apex_predators)}")

def find_producers(data):
    """Identify producers."""
    producers = [predator for predator, prey in data.items() if not prey]
    print(f"Producers: {formatList(producers)}")

def find_most_flexible_eaters(data):
    """Identify the most flexible eaters."""
    max_prey_count = max(len(prey) for prey in data.values())
    flexible_eaters = [predator for predator, prey in data.items() if len(prey) == max_prey_count]
    print(f"Most Flexible Eaters: {formatList(flexible_eaters)}")

def find_tastiest_organisms(data):
    """Identify the tastiest organisms."""
    prey_count = {}
    for prey_list in data.values():
        for prey in prey_list:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values(), default=0)
    tastiest = [prey for prey, count in prey_count.items() if count == max_count]
    print(f"Tastiest: {formatList(tastiest)}")

def determine_heights(data):
    """Determine the height of each organism in the food web."""
    heights = {organism: 0 for organism in data}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in data.items():
            for prey in prey_list:
                if heights[predator] <= heights.get(prey, 0):
                    heights[predator] = heights.get(prey, 0) + 1
                    changed = True
    print("Heights:")
    for organism in sorted(heights.keys()):
        print(f"  {organism}: {heights[organism]}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python food_web_analyzer.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    data = load_data(filename)
    list_predators_and_prey(data)
    find_apex_predators(data)
    find_producers(data)
    find_most_flexible_eaters(data)
    find_tastiest_organisms(data)
    determine_heights(data)

if __name__ == "__main__":
    main()