import sys
from formatList import formatList

def load_food_web(filename):
    food_web = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
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
    print()

def get_apex_predators(food_web):
    all_prey = set(prey for prey_list in food_web.values() for prey in prey_list)
    return sorted(set(food_web.keys()) - all_prey)

def get_producers(food_web):
    all_animals = set(food_web.keys()) | set(prey for prey_list in food_web.values() for prey in prey_list)
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

def main():
    if len(sys.argv) != 2:
        filename = input("Enter the name of the food web file: ")
    else:
        filename = sys.argv[1]
    
    food_web = load_food_web(filename)
    
    display_predators_and_prey(food_web)
    
    print("Apex Predators:", formatList(get_apex_predators(food_web)))
    print("Producers:", formatList(get_producers(food_web)))
    print("Most Flexible Eaters:", formatList(get_most_flexible_eaters(food_web)))
    print("Tastiest:", formatList(get_tastiest(food_web)))
    print()
    
    print("Heights:")
    for animal, height in sorted(get_heights(food_web).items()):
        print(f"  {animal}: {height}")

if __name__ == "__main__":
    main()