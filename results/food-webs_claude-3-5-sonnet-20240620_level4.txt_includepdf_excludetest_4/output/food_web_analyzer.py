import sys
from formatList import formatList

def load_food_web(filename):
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
    print("Predators and Prey:")
    for predator, prey in sorted(food_web.items()):
        print(f"  {predator} eats {formatList(prey)}")

def find_apex_predators(food_web):
    all_animals = set(food_web.keys()).union(set(prey for prey_list in food_web.values() for prey in prey_list))
    prey_animals = set(prey for prey_list in food_web.values() for prey in prey_list)
    return sorted(all_animals - prey_animals)

def find_producers(food_web):
    all_animals = set(food_web.keys()).union(set(prey for prey_list in food_web.values() for prey in prey_list))
    predators = set(food_web.keys())
    return sorted(all_animals - predators)

def find_most_flexible_eaters(food_web):
    max_prey = max(len(prey) for prey in food_web.values())
    return sorted([predator for predator, prey in food_web.items() if len(prey) == max_prey])

def find_tastiest_organisms(food_web):
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

def analyze_food_web(filename):
    food_web = load_food_web(filename)
    
    display_predators_and_prey(food_web)
    print()
    
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
    herbivores, omnivores, carnivores = classify_animals(food_web, producers)
    print("\nFor an A+:")
    print(f"  Herbivores: {formatList(herbivores)}")
    print(f"  Omnivores: {formatList(omnivores)}")
    print(f"  Carnivores: {formatList(carnivores)}")

def classify_animals(food_web, producers):
    herbivores = []
    omnivores = []
    carnivores = []

    for predator, prey in food_web.items():
        if all(p in producers for p in prey):
            herbivores.append(predator)
        elif any(p in producers for p in prey) and any(p not in producers for p in prey):
            omnivores.append(predator)
        else:
            carnivores.append(predator)

    return sorted(herbivores), sorted(omnivores), sorted(carnivores)