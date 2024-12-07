import sys
from formatList import formatList

def load_food_web(filename):
    food_web = {}
    with open(filename, 'r') as file:
        for line in file:
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

def get_apex_predators(food_web):
    all_prey = set()
    for prey_list in food_web.values():
        all_prey.update(prey_list)
    return sorted(set(food_web.keys()) - all_prey)

def get_producers(food_web):
    all_animals = set(food_web.keys()).union(set(prey for prey_list in food_web.values() for prey in prey_list))
    return sorted(all_animals - set(food_web.keys()))

def get_most_flexible_eaters(food_web):
    max_prey = max(len(prey) for prey in food_web.values())
    return sorted(predator for predator, prey in food_web.items() if len(prey) == max_prey)

def get_tastiest_organisms(food_web):
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values())
    return sorted(prey for prey, count in prey_count.items() if count == max_count)

def get_heights(food_web):
    heights = {animal: 0 for animal in set(food_web.keys()).union(set(prey for prey_list in food_web.values() for prey in prey_list))}
    
    changed = True
    while changed:
        changed = False
        for predator, prey_list in food_web.items():
            for prey in prey_list:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    
    return heights

def main():
    if len(sys.argv) != 2:
        print("Usage: python Assignment4.py <food_web_file>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        food_web = load_food_web(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    display_predators_and_prey(food_web)

    apex_predators = get_apex_predators(food_web)
    print(f"Apex Predators: {formatList(apex_predators)}\n")

    producers = get_producers(food_web)
    print(f"Producers: {formatList(producers)}\n")

    most_flexible_eaters = get_most_flexible_eaters(food_web)
    print(f"Most Flexible Eaters: {formatList(most_flexible_eaters)}\n")

    tastiest_organisms = get_tastiest_organisms(food_web)
    print(f"Tastiest: {formatList(tastiest_organisms)}\n")

    heights = get_heights(food_web)
    print("Heights:")
    for animal, height in sorted(heights.items()):
        print(f"  {animal}: {height}")

if __name__ == "__main__":
    main()