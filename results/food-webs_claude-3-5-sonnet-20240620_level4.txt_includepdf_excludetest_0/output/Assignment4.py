import sys
from formatList import formatList

def load_food_web(filename):
    """
    Load the food web data from a file into a dictionary.
    
    Parameters:
    filename (str): The name of the file to read from.
    
    Returns:
    dict: A dictionary where keys are predators and values are lists of prey.
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
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)
    return food_web

def display_predators_and_prey(food_web):
    """
    Display the predators and their prey.
    
    Parameters:
    food_web (dict): The food web dictionary.
    """
    print("Predators and Prey:")
    for predator, prey in sorted(food_web.items()):
        print(f"  {predator} eats {formatList(prey)}")
    print()

def identify_apex_predators(food_web):
    """
    Identify and display the apex predators.
    
    Parameters:
    food_web (dict): The food web dictionary.
    """
    all_prey = set()
    for prey_list in food_web.values():
        all_prey.update(prey_list)
    
    apex_predators = [predator for predator in food_web.keys() if predator not in all_prey]
    print(f"Apex Predators: {formatList(sorted(apex_predators))}")
    print()

def identify_producers(food_web):
    """
    Identify and display the producers.
    
    Parameters:
    food_web (dict): The food web dictionary.
    """
    all_animals = set(food_web.keys()).union(*food_web.values())
    producers = [animal for animal in all_animals if animal not in food_web]
    print(f"Producers: {formatList(sorted(producers))}")
    print()

def identify_most_flexible_eaters(food_web):
    """
    Identify and display the most flexible eaters.
    
    Parameters:
    food_web (dict): The food web dictionary.
    """
    max_prey = max(len(prey) for prey in food_web.values())
    flexible_eaters = [predator for predator, prey in food_web.items() if len(prey) == max_prey]
    print(f"Most Flexible Eaters: {formatList(sorted(flexible_eaters))}")
    print()

def identify_tastiest_organisms(food_web):
    """
    Identify and display the tastiest organisms.
    
    Parameters:
    food_web (dict): The food web dictionary.
    """
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    
    max_count = max(prey_count.values())
    tastiest = [prey for prey, count in prey_count.items() if count == max_count]
    print(f"Tastiest: {formatList(sorted(tastiest))}")
    print()

def determine_heights(food_web):
    """
    Determine and display the height of each organism in the food web.
    
    Parameters:
    food_web (dict): The food web dictionary.
    """
    all_animals = set(food_web.keys()).union(*food_web.values())
    heights = {animal: 0 for animal in all_animals}
    
    changed = True
    while changed:
        changed = False
        for predator, prey_list in food_web.items():
            for prey in prey_list:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    
    print("Heights:")
    for animal, height in sorted(heights.items()):
        print(f"  {animal}: {height}")
    print()

def identify_herbivores_omnivores_carnivores(food_web):
    """
    Identify and display herbivores, omnivores, and carnivores.
    
    Parameters:
    food_web (dict): The food web dictionary.
    """
    all_animals = set(food_web.keys()).union(*food_web.values())
    producers = set(animal for animal in all_animals if animal not in food_web)
    
    herbivores = []
    omnivores = []
    carnivores = []
    
    for predator, prey_list in food_web.items():
        eats_plants = any(prey in producers for prey in prey_list)
        eats_animals = any(prey not in producers for prey in prey_list)
        
        if eats_plants and not eats_animals:
            herbivores.append(predator)
        elif eats_plants and eats_animals:
            omnivores.append(predator)
        elif not eats_plants and eats_animals:
            carnivores.append(predator)
    
    print("For an A+:")
    print(f"  Herbivores: {formatList(sorted(herbivores))}")
    print(f"  Omnivores: {formatList(sorted(omnivores))}")
    print(f"  Carnivores: {formatList(sorted(carnivores))}")

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
    identify_apex_predators(food_web)
    identify_producers(food_web)
    identify_most_flexible_eaters(food_web)
    identify_tastiest_organisms(food_web)
    determine_heights(food_web)
    identify_herbivores_omnivores_carnivores(food_web)

if __name__ == "__main__":
    main()