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
    all_prey = set(animal for prey_list in food_web.values() for animal in prey_list)
    return sorted(set(food_web.keys()) - all_prey)

def get_producers(food_web):
    all_animals = set(food_web.keys()) | set(animal for prey_list in food_web.values() for animal in prey_list)
    return sorted(all_animals - set(food_web.keys()))

def get_most_flexible_eaters(food_web):
    max_prey = max(len(prey) for prey in food_web.values())
    return sorted(predator for predator, prey in food_web.items() if len(prey) == max_prey)

def get_tastiest(food_web):
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values())
    return sorted(prey for prey, count in prey_count.items() if count == max_count)

def get_heights(food_web):
    heights = {animal: 0 for animal in get_producers(food_web)}
    
    def get_height(animal):
        if animal in heights:
            return heights[animal]
        
        max_prey_height = max(get_height(prey) for prey in food_web.get(animal, []))
        heights[animal] = max_prey_height + 1
        return heights[animal]
    
    for animal in food_web:
        get_height(animal)
    
    return heights

def get_herbivores_omnivores_carnivores(food_web, producers):
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
    
    return sorted(herbivores), sorted(omnivores), sorted(carnivores)

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
    
    apex_predators = get_apex_predators(food_web)
    print("Apex Predators:", formatList(apex_predators))
    print()
    
    producers = get_producers(food_web)
    print("Producers:", formatList(producers))
    print()
    
    most_flexible = get_most_flexible_eaters(food_web)
    print("Most Flexible Eaters:", formatList(most_flexible))
    print()
    
    tastiest = get_tastiest(food_web)
    print("Tastiest:", formatList(tastiest))
    print()
    
    heights = get_heights(food_web)
    print("Heights:")
    for animal, height in sorted(heights.items()):
        print(f"  {animal}: {height}")
    print()
    
    herbivores, omnivores, carnivores = get_herbivores_omnivores_carnivores(food_web, producers)
    print("For an A+:")
    print("  Herbivores:", formatList(herbivores))
    print("  Omnivores:", formatList(omnivores))
    print("  Carnivores:", formatList(carnivores))

if __name__ == "__main__":
    main()