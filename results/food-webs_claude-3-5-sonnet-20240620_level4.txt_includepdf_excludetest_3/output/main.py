import sys
from formatList import formatList

def read_food_web(filename):
    """
    Read the food web data from the given file and return a dictionary
    representing the predator-prey relationships.
    """
    food_web = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                animals = line.strip().split(',')
                predator = animals[0]
                prey = animals[1:]
                food_web[predator] = prey
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    return food_web

def display_predators_and_prey(food_web):
    """
    Display the predators and their prey from the food web.
    """
    print("Predators and Prey:")
    for predator, prey in sorted(food_web.items()):
        print(f"  {predator} eats {formatList(prey)}")
    print()

def find_apex_predators(food_web):
    """
    Find and return a list of apex predators in the food web.
    """
    all_prey = set()
    for prey_list in food_web.values():
        all_prey.update(prey_list)
    return [predator for predator in food_web.keys() if predator not in all_prey]

def find_producers(food_web):
    """
    Find and return a list of producers in the food web.
    """
    all_animals = set(food_web.keys()).union(set(prey for prey_list in food_web.values() for prey in prey_list))
    return [animal for animal in all_animals if animal not in food_web]

def find_most_flexible_eaters(food_web):
    """
    Find and return a list of the most flexible eaters in the food web.
    """
    max_prey = max(len(prey) for prey in food_web.values())
    return [predator for predator, prey in food_web.items() if len(prey) == max_prey]

def find_tastiest_organisms(food_web):
    """
    Find and return a list of the tastiest organisms in the food web.
    """
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values())
    return [prey for prey, count in prey_count.items() if count == max_count]

def calculate_heights(food_web):
    """
    Calculate and return the heights of all organisms in the food web.
    """
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

def find_herbivores_omnivores_carnivores(food_web, producers):
    """
    Find and return lists of herbivores, omnivores, and carnivores in the food web.
    """
    herbivores = []
    omnivores = []
    carnivores = []

    for predator, prey in food_web.items():
        eats_plants = any(p in producers for p in prey)
        eats_animals = any(p not in producers for p in prey)
        
        if eats_plants and not eats_animals:
            herbivores.append(predator)
        elif eats_plants and eats_animals:
            omnivores.append(predator)
        elif not eats_plants and eats_animals:
            carnivores.append(predator)

    return herbivores, omnivores, carnivores

def main():
    if len(sys.argv) != 2:
        if len(sys.argv) > 2:
            print("Error: Too many command line arguments.")
            sys.exit(1)
        filename = input("Enter the name of the food web file: ")
    else:
        filename = sys.argv[1]

    food_web = read_food_web(filename)

    display_predators_and_prey(food_web)

    apex_predators = find_apex_predators(food_web)
    print(f"Apex Predators: {formatList(apex_predators)}")

    producers = find_producers(food_web)
    print(f"Producers: {formatList(producers)}")

    most_flexible_eaters = find_most_flexible_eaters(food_web)
    print(f"Most Flexible Eaters: {formatList(most_flexible_eaters)}")

    tastiest_organisms = find_tastiest_organisms(food_web)
    print(f"Tastiest: {formatList(tastiest_organisms)}")

    heights = calculate_heights(food_web)
    print("\nHeights:")
    for animal, height in sorted(heights.items()):
        print(f"  {animal}: {height}")

    # A+ part
    herbivores, omnivores, carnivores = find_herbivores_omnivores_carnivores(food_web, producers)
    print("\nFor an A+:")
    print(f"  Herbivores: {formatList(sorted(herbivores))}")
    print(f"  Omnivores: {formatList(sorted(omnivores))}")
    print(f"  Carnivores: {formatList(sorted(carnivores))}")

if __name__ == "__main__":
    main()