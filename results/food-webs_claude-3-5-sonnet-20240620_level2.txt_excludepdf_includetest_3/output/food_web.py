import sys
from format_list import format_list

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

def print_predator_prey(food_web):
    print("Predators and Prey:")
    for predator, prey in sorted(food_web.items()):
        print(f"  {predator} eats {format_list(prey)}")

def find_apex_predators(food_web):
    all_prey = set()
    for prey_list in food_web.values():
        all_prey.update(prey_list)
    return set(food_web.keys()) - all_prey

def find_producers(food_web):
    all_animals = set(food_web.keys()).union(set(prey for prey_list in food_web.values() for prey in prey_list))
    return all_animals - set(food_web.keys())

def find_most_flexible_eaters(food_web):
    max_prey = max(len(prey) for prey in food_web.values())
    return [pred for pred, prey in food_web.items() if len(prey) == max_prey]

def find_tastiest(food_web):
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values())
    return [prey for prey, count in prey_count.items() if count == max_count]

def calculate_heights(food_web):
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
        if len(sys.argv) > 2:
            print("Error: Too many command line arguments.")
            sys.exit(1)
        filename = input("Enter the name of the food web file: ")
    else:
        filename = sys.argv[1]
    
    food_web = load_food_web(filename)
    
    print_predator_prey(food_web)
    print()
    
    apex_predators = find_apex_predators(food_web)
    print(f"Apex Predators: {format_list(sorted(apex_predators))}")
    print()
    
    producers = find_producers(food_web)
    print(f"Producers: {format_list(sorted(producers))}")
    print()
    
    most_flexible = find_most_flexible_eaters(food_web)
    print(f"Most Flexible Eaters: {format_list(sorted(most_flexible))}")
    print()
    
    tastiest = find_tastiest(food_web)
    print(f"Tastiest: {format_list(sorted(tastiest))}")
    print()
    
    heights = calculate_heights(food_web)
    print("Heights:")
    for animal, height in sorted(heights.items()):
        print(f"  {animal}: {height}")

if __name__ == "__main__":
    main()