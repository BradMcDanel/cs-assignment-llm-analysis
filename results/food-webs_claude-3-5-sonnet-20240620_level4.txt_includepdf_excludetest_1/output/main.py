import sys
from formatList import formatList

def load_food_web(filename):
    """
    Load the food web data from a file into a dictionary.
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
    Display the predators and their prey.
    """
    print("Predators and Prey:")
    for predator, prey in sorted(food_web.items()):
        print(f"  {predator} eats {formatList(prey)}")
    print()

def find_apex_predators(food_web):
    """
    Find and return the apex predators in the food web.
    """
    all_animals = set(food_web.keys()).union(set(prey for preys in food_web.values() for prey in preys))
    return [animal for animal in all_animals if animal not in set(prey for preys in food_web.values() for prey in preys)]

def find_producers(food_web):
    """
    Find and return the producers in the food web.
    """
    all_animals = set(food_web.keys()).union(set(prey for preys in food_web.values() for prey in preys))
    return [animal for animal in all_animals if animal not in food_web]

def find_most_flexible_eaters(food_web):
    """
    Find and return the most flexible eaters in the food web.
    """
    max_prey = max(len(prey) for prey in food_web.values())
    return [predator for predator, prey in food_web.items() if len(prey) == max_prey]

def find_tastiest_organisms(food_web):
    """
    Find and return the tastiest organisms in the food web.
    """
    prey_count = {}
    for preys in food_web.values():
        for prey in preys:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values())
    return [prey for prey, count in prey_count.items() if count == max_count]

def calculate_heights(food_web):
    """
    Calculate and return the heights of all organisms in the food web.
    """
    heights = {animal: 0 for animal in set(food_web.keys()).union(set(prey for preys in food_web.values() for prey in preys))}
    changed = True
    while changed:
        changed = False
        for predator, preys in food_web.items():
            for prey in preys:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    return heights

def classify_animals(food_web):
    """
    Classify animals as herbivores, omnivores, or carnivores.
    """
    producers = set(find_producers(food_web))
    herbivores = []
    omnivores = []
    carnivores = []

    for predator, preys in food_web.items():
        eats_plants = any(prey in producers for prey in preys)
        eats_animals = any(prey not in producers for prey in preys)
        
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

    food_web = load_food_web(filename)

    display_predators_and_prey(food_web)

    apex_predators = find_apex_predators(food_web)
    print(f"Apex Predators: {formatList(sorted(apex_predators))}")

    producers = find_producers(food_web)
    print(f"Producers: {formatList(sorted(producers))}")

    flexible_eaters = find_most_flexible_eaters(food_web)
    print(f"Most Flexible Eaters: {formatList(sorted(flexible_eaters))}")

    tastiest = find_tastiest_organisms(food_web)
    print(f"Tastiest: {formatList(sorted(tastiest))}")

    heights = calculate_heights(food_web)
    print("\nHeights:")
    for animal, height in sorted(heights.items()):
        print(f"  {animal}: {height}")

    # A+ part
    herbivores, omnivores, carnivores = classify_animals(food_web)
    print("\nFor an A+:")
    print(f"  Herbivores: {formatList(sorted(herbivores))}")
    print(f"  Omnivores: {formatList(sorted(omnivores))}")
    print(f"  Carnivores: {formatList(sorted(carnivores))}")

if __name__ == "__main__":
    main()