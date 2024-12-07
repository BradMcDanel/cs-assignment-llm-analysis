import sys

def load_food_web(file_name):
    """
    Load the predator-prey relationships from a file and store them in a dictionary.
    
    :param file_name: The name of the file containing the predator-prey data.
    :return: A dictionary with predators as keys and a list of their prey as values.
    """
    food_web = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                food_web[predator] = prey
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        sys.exit(1)
    
    return food_web

def format_predator_prey(food_web):
    """
    Display each predator and what they eat in a formatted manner.
    
    :param food_web: The dictionary containing predator-prey relationships.
    """
    print("Predators and Prey:")
    for predator, prey_list in sorted(food_web.items()):
        if len(prey_list) > 1:
            prey_str = ', '.join(prey_list[:-1]) + " and " + prey_list[-1]
        else:
            prey_str = prey_list[0]
        print(f"  {predator} eats {prey_str}")

def find_apex_predators(food_web):
    """
    Identify and display apex predators.
    
    :param food_web: The dictionary containing predator-prey relationships.
    """
    all_prey = {prey for prey_list in food_web.values() for prey in prey_list}
    apex_predators = [predator for predator in food_web.keys() if predator not in all_prey]
    print(f"Apex Predators: {', '.join(sorted(apex_predators))}")

def find_producers(food_web):
    """
    Identify and display producers.
    
    :param food_web: The dictionary containing predator-prey relationships.
    """
    producers = [predator for predator, prey_list in food_web.items() if not prey_list]
    print(f"Producers: {', '.join(sorted(producers))}")

def find_most_flexible_eaters(food_web):
    """
    Identify and display the most flexible eaters.
    
    :param food_web: The dictionary containing predator-prey relationships.
    """
    max_prey_count = max(len(prey) for prey in food_web.values())
    most_flexible_eaters = [predator for predator, prey in food_web.items() if len(prey) == max_prey_count]
    print(f"Most Flexible Eaters: {', '.join(sorted(most_flexible_eaters))}")

def find_tastiest_organisms(food_web):
    """
    Identify and display the tastiest organisms.
    
    :param food_web: The dictionary containing predator-prey relationships.
    """
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            if prey in prey_count:
                prey_count[prey] += 1
            else:
                prey_count[prey] = 1
    max_count = max(prey_count.values())
    tastiest_organisms = [prey for prey, count in prey_count.items() if count == max_count]
    print(f"Tastiest: {', '.join(sorted(tastiest_organisms))}")

def calculate_heights(food_web):
    """
    Calculate and display the height of each organism in the food web.
    
    :param food_web: The dictionary containing predator-prey relationships.
    """
    heights = {animal: 0 for animal in food_web.keys()}
    changed = True
    
    while changed:
        changed = False
        for predator, prey_list in food_web.items():
            for prey in prey_list:
                if heights[predator] <= heights.get(prey, 0):
                    heights[predator] = heights.get(prey, 0) + 1
                    changed = True
    
    print("Heights:")
    for animal, height in sorted(heights.items()):
        print(f"  {animal}: {height}")

def main():
    if len(sys.argv) != 2:
        file_name = input("Please enter the food web file name: ")
    else:
        file_name = sys.argv[1]

    food_web = load_food_web(file_name)
    format_predator_prey(food_web)
    find_apex_predators(food_web)
    find_producers(food_web)
    find_most_flexible_eaters(food_web)
    find_tastiest_organisms(food_web)
    calculate_heights(food_web)

if __name__ == "__main__":
    main()