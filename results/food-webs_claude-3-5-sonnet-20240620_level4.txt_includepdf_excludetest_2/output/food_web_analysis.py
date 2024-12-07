import sys
from formatList import formatList

def load_food_web(filename):
    food_web = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                predator, *prey = line.strip().split(',')
                food_web[predator] = prey
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    return food_web

def display_predators_and_prey(food_web):
    print("Predators and Prey:")
    for predator, prey in sorted(food_web.items()):
        print(f"  {predator} eats {formatList(prey)}")

def find_apex_predators(food_web):
    all_prey = set(animal for prey_list in food_web.values() for animal in prey_list)
    apex_predators = [predator for predator in food_web.keys() if predator not in all_prey]
    return apex_predators

def find_producers(food_web):
    all_animals = set(food_web.keys()) | set(animal for prey_list in food_web.values() for animal in prey_list)
    producers = [animal for animal in all_animals if animal not in food_web]
    return producers

def find_most_flexible_eaters(food_web):
    max_prey = max(len(prey) for prey in food_web.values())
    return [predator for predator, prey in food_web.items() if len(prey) == max_prey]

def find_tastiest_organisms(food_web):
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values())
    return [prey for prey, count in prey_count.items() if count == max_count]

def calculate_heights(food_web):
    heights = {animal: 0 for animal in set(food_web.keys()) | set(animal for prey_list in food_web.values() for animal in prey_list)}
    
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

    display_predators_and_prey(food_web)
    print()

    apex_predators = find_apex_predators(food_web)
    print(f"Apex Predators: {formatList(sorted(apex_predators))}")

    producers = find_producers(food_web)
    print(f"Producers: {formatList(sorted(producers))}")

    most_flexible_eaters = find_most_flexible_eaters(food_web)
    print(f"Most Flexible Eaters: {formatList(sorted(most_flexible_eaters))}")

    tastiest_organisms = find_tastiest_organisms(food_web)
    print(f"Tastiest: {formatList(sorted(tastiest_organisms))}")

    heights = calculate_heights(food_web)
    print("\nHeights:")
    for animal, height in sorted(heights.items()):
        print(f"  {animal}: {height}")

if __name__ == "__main__":
    main()