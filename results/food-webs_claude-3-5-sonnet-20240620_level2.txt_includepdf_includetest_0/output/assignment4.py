import sys
from formatList import formatList

def load_food_web(filename):
    food_web = {}
    with open(filename, 'r') as f:
        for line in f:
            animals = line.strip().split(',')
            predator = animals[0]
            prey = animals[1:]
            food_web[predator] = prey
    return food_web

def display_predators_and_prey(food_web):
    print("Predators and Prey:")
    for predator, prey in sorted(food_web.items()):
        print(f"  {predator} eats {formatList(prey)}")
    print()

def find_apex_predators(food_web):
    all_animals = set(food_web.keys()).union(set(prey for preys in food_web.values() for prey in preys))
    apex_predators = all_animals - set(prey for preys in food_web.values() for prey in preys)
    print(f"Apex Predators: {formatList(sorted(apex_predators))}")
    print()

def find_producers(food_web):
    all_animals = set(food_web.keys()).union(set(prey for preys in food_web.values() for prey in preys))
    producers = all_animals - set(food_web.keys())
    print(f"Producers: {formatList(sorted(producers))}")
    print()

def find_most_flexible_eaters(food_web):
    max_prey = max(len(prey) for prey in food_web.values())
    flexible_eaters = [pred for pred, prey in food_web.items() if len(prey) == max_prey]
    print(f"Most Flexible Eaters: {formatList(sorted(flexible_eaters))}")
    print()

def find_tastiest_organisms(food_web):
    prey_count = {}
    for preys in food_web.values():
        for prey in preys:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values())
    tastiest = [prey for prey, count in prey_count.items() if count == max_count]
    print(f"Tastiest: {formatList(sorted(tastiest))}")
    print()

def calculate_heights(food_web):
    heights = {animal: 0 for animal in set(food_web.keys()).union(set(prey for preys in food_web.values() for prey in preys))}
    
    changed = True
    while changed:
        changed = False
        for predator, preys in food_web.items():
            for prey in preys:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    
    print("Heights:")
    for animal, height in sorted(heights.items()):
        print(f"  {animal}: {height}")
    print()

def main():
    if len(sys.argv) != 2:
        print("Usage: python assignment4.py <food_web_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    try:
        food_web = load_food_web(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    
    display_predators_and_prey(food_web)
    find_apex_predators(food_web)
    find_producers(food_web)
    find_most_flexible_eaters(food_web)
    find_tastiest_organisms(food_web)
    calculate_heights(food_web)

if __name__ == "__main__":
    main()