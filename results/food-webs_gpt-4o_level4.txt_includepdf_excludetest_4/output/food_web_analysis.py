import sys
from formatList import formatList

def load_food_web(filename):
    """Load the predator-prey relationships from a file into a dictionary."""
    try:
        with open(filename, 'r') as file:
            food_web = {}
            for line in file:
                parts = line.strip().split(',')
                predator, prey = parts[0], parts[1:]
                food_web[predator] = prey
            return food_web
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)

def list_predators_and_prey(food_web):
    """List each predator and what it eats."""
    print("Predators and Prey:")
    for predator in sorted(food_web.keys()):
        prey = formatList(food_web[predator])
        print(f"  {predator} eats {prey}")

def identify_apex_predators(food_web):
    """Identify apex predators."""
    all_prey = set(prey for preys in food_web.values() for prey in preys)
    apex_predators = [predator for predator in food_web if predator not in all_prey]
    print(f"Apex Predators: {formatList(apex_predators)}")

def identify_producers(food_web):
    """Identify producers."""
    producers = [organism for organism in food_web if len(food_web[organism]) == 0]
    print(f"Producers: {formatList(producers)}")

def identify_most_flexible_eaters(food_web):
    """Identify the most flexible eaters."""
    max_eats = max(len(prey) for prey in food_web.values())
    flexible_eaters = [predator for predator, prey in food_web.items() if len(prey) == max_eats]
    print(f"Most Flexible Eaters: {formatList(flexible_eaters)}")

def identify_tastiest_organisms(food_web):
    """Identify the tastiest organism."""
    eat_counts = {}
    for predator in food_web:
        for prey in food_web[predator]:
            if prey not in eat_counts:
                eat_counts[prey] = 0
            eat_counts[prey] += 1
    max_eaten = max(eat_counts.values())
    tastiest = [organism for organism, count in eat_counts.items() if count == max_eaten]
    print(f"Tastiest: {formatList(tastiest)}")

def determine_heights(food_web):
    """Determine the height of each organism in the food web."""
    heights = {organism: 0 for organism in food_web}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in food_web.items():
            for prey in prey_list:
                if prey in heights and heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    print("Heights:")
    for organism in sorted(heights.keys()):
        print(f"  {organism}: {heights[organism]}")

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input("Enter the name of the food web file: ")

    food_web = load_food_web(filename)
    list_predators_and_prey(food_web)
    identify_apex_predators(food_web)
    identify_producers(food_web)
    identify_most_flexible_eaters(food_web)
    identify_tastiest_organisms(food_web)
    determine_heights(food_web)

if __name__ == "__main__":
    main()