import sys
import formatList

def load_food_web(filename):
    food_web = {}
    with open(filename, 'r') as file:
        for line in file:
            predator, *prey = line.strip().split(',')
            food_web[predator] = prey
    return food_web

def display_predators_and_prey(food_web):
    print("Predators and Prey:")
    for predator, prey in sorted(food_web.items()):
        print(f"  {predator} eats {formatList.formatList(prey)}")
    print()

def find_apex_predators(food_web):
    all_prey = set(prey for preys in food_web.values() for prey in preys)
    apex_predators = [predator for predator in food_web.keys() if predator not in all_prey]
    return apex_predators

def find_producers(food_web):
    all_animals = set(food_web.keys()) | set(prey for preys in food_web.values() for prey in preys)
    producers = [animal for animal in all_animals if animal not in food_web]
    return producers

def find_most_flexible_eaters(food_web):
    max_prey = max(len(prey) for prey in food_web.values())
    return [predator for predator, prey in food_web.items() if len(prey) == max_prey]

def find_tastiest_organisms(food_web):
    prey_count = {}
    for preys in food_web.values():
        for prey in preys:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values())
    return [prey for prey, count in prey_count.items() if count == max_count]

def calculate_heights(food_web):
    heights = {animal: 0 for animal in set(food_web.keys()) | set(prey for preys in food_web.values() for prey in preys)}
    
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
    if len(sys.argv) != 2:
        if len(sys.argv) > 2:
            print("Error: Too many command line arguments.")
            sys.exit(1)
        filename = input("Enter the name of the food web file: ")
    else:
        filename = sys.argv[1]

    try:
        food_web = load_food_web(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    display_predators_and_prey(food_web)

    apex_predators = find_apex_predators(food_web)
    print("Apex Predators:", formatList.formatList(sorted(apex_predators)))
    print()

    producers = find_producers(food_web)
    print("Producers:", formatList.formatList(sorted(producers)))
    print()

    most_flexible_eaters = find_most_flexible_eaters(food_web)
    print("Most Flexible Eaters:", formatList.formatList(sorted(most_flexible_eaters)))
    print()

    tastiest_organisms = find_tastiest_organisms(food_web)
    print("Tastiest:", formatList.formatList(sorted(tastiest_organisms)))
    print()

    heights = calculate_heights(food_web)
    print("Heights:")
    for animal, height in sorted(heights.items()):
        print(f"  {animal}: {height}")

if __name__ == "__main__":
    main()