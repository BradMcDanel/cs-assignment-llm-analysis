import sys
from formatList import formatList

def load_food_web(filename):
    food_web = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                animals = line.strip().split(',')
                predator = animals[0]
                prey = animals[1:]
                food_web[predator] = prey
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    return food_web

def print_predators_and_prey(food_web):
    print("Predators and Prey:")
    for predator, prey in sorted(food_web.items()):
        print(f"  {predator} eats {formatList(prey)}")
    print()

def get_apex_predators(food_web):
    all_animals = set(food_web.keys()).union(set(animal for prey in food_web.values() for animal in prey))
    prey_animals = set(animal for prey in food_web.values() for animal in prey)
    return all_animals - prey_animals

def print_apex_predators(apex_predators):
    print(f"Apex Predators: {formatList(sorted(apex_predators))}")
    print()

def get_producers(food_web):
    all_animals = set(food_web.keys()).union(set(animal for prey in food_web.values() for animal in prey))
    predators = set(food_web.keys())
    return all_animals - predators

def print_producers(producers):
    print(f"Producers: {formatList(sorted(producers))}")
    print()

def get_most_flexible_eaters(food_web):
    max_prey = max(len(prey) for prey in food_web.values())
    return [predator for predator, prey in food_web.items() if len(prey) == max_prey]

def print_most_flexible_eaters(flexible_eaters):
    print(f"Most Flexible Eaters: {formatList(sorted(flexible_eaters))}")
    print()

def get_tastiest_organisms(food_web):
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values())
    return [prey for prey, count in prey_count.items() if count == max_count]

def print_tastiest_organisms(tastiest):
    print(f"Tastiest: {formatList(sorted(tastiest))}")
    print()

def get_heights(food_web):
    heights = {animal: 0 for animal in set(food_web.keys()).union(set(animal for prey in food_web.values() for animal in prey))}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in food_web.items():
            for prey in prey_list:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    return heights

def print_heights(heights):
    print("Heights:")
    for animal, height in sorted(heights.items()):
        print(f"  {animal}: {height}")
    print()

def main():
    if len(sys.argv) != 2:
        if len(sys.argv) > 2:
            print("Error: Too many command line arguments.")
            sys.exit(1)
        filename = input("Enter the name of the food web file: ")
    else:
        filename = sys.argv[1]

    food_web = load_food_web(filename)
    
    print_predators_and_prey(food_web)
    
    apex_predators = get_apex_predators(food_web)
    print_apex_predators(apex_predators)
    
    producers = get_producers(food_web)
    print_producers(producers)
    
    flexible_eaters = get_most_flexible_eaters(food_web)
    print_most_flexible_eaters(flexible_eaters)
    
    tastiest = get_tastiest_organisms(food_web)
    print_tastiest_organisms(tastiest)
    
    heights = get_heights(food_web)
    print_heights(heights)

if __name__ == "__main__":
    main()