import sys
import formatList

def read_food_web(filename):
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
        print(f"  {predator} eats {formatList.formatList(prey)}")
    print()

def find_apex_predators(food_web):
    all_animals = set(food_web.keys()).union(set(prey for prey_list in food_web.values() for prey in prey_list))
    prey_animals = set(prey for prey_list in food_web.values() for prey in prey_list)
    apex_predators = all_animals - prey_animals
    return sorted(apex_predators)

def find_producers(food_web):
    all_animals = set(food_web.keys()).union(set(prey for prey_list in food_web.values() for prey in prey_list))
    predators = set(food_web.keys())
    producers = all_animals - predators
    return sorted(producers)

def find_most_flexible_eaters(food_web):
    max_prey = max(len(prey) for prey in food_web.values())
    return sorted([predator for predator, prey in food_web.items() if len(prey) == max_prey])

def find_tastiest(food_web):
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values())
    return sorted([prey for prey, count in prey_count.items() if count == max_count])

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

    try:
        food_web = read_food_web(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    display_predators_and_prey(food_web)

    apex_predators = find_apex_predators(food_web)
    print("Apex Predators:", formatList.formatList(apex_predators))
    print()

    producers = find_producers(food_web)
    print("Producers:", formatList.formatList(producers))
    print()

    most_flexible_eaters = find_most_flexible_eaters(food_web)
    print("Most Flexible Eaters:", formatList.formatList(most_flexible_eaters))
    print()

    tastiest = find_tastiest(food_web)
    print("Tastiest:", formatList.formatList(tastiest))
    print()

    heights = calculate_heights(food_web)
    print("Heights:")
    for animal, height in sorted(heights.items()):
        print(f"  {animal}: {height}")

if __name__ == "__main__":
    main()