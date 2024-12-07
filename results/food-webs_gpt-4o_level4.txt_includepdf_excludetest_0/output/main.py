import sys
from formatList import formatList

def load_food_web(file_path):
    # Load the predator-prey relationships from the file into a dictionary
    food_web = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                food_web[predator] = prey
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        sys.exit(1)
    
    return food_web

def display_predators_and_prey(food_web):
    print("Predators and Prey:")
    for predator, prey_list in sorted(food_web.items()):
        formatted_prey = formatList(prey_list)
        print(f"  {predator} eats {formatted_prey}")

def identify_apex_predators(food_web):
    all_prey = set(prey for prey_list in food_web.values() for prey in prey_list)
    apex_predators = [predator for predator in food_web if predator not in all_prey]
    return apex_predators

def identify_producers(food_web):
    producers = [species for species, prey_list in food_web.items() if len(prey_list) == 0]
    return producers

def identify_most_flexible_eaters(food_web):
    max_prey_count = max(len(prey_list) for prey_list in food_web.values())
    flexible_eaters = [predator for predator, prey_list in food_web.items() if len(prey_list) == max_prey_count]
    return flexible_eaters

def identify_tastiest_organisms(food_web):
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            if prey in prey_count:
                prey_count[prey] += 1
            else:
                prey_count[prey] = 1
    max_preyed_count = max(prey_count.values())
    tastiest = [prey for prey, count in prey_count.items() if count == max_preyed_count]
    return tastiest

def calculate_heights(food_web):
    heights = {species: 0 for species in food_web}
    changed = True
    while changed:
        changed = False
        for predator in food_web:
            for prey in food_web[predator]:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    return heights

def main():
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    elif len(sys.argv) > 2:
        print("Error: Too many command line arguments.")
        sys.exit(1)
    else:
        file_path = input("Enter the food web file name: ")

    food_web = load_food_web(file_path)

    display_predators_and_prey(food_web)

    apex_predators = identify_apex_predators(food_web)
    print(f"Apex Predators: {formatList(apex_predators)}")

    producers = identify_producers(food_web)
    print(f"Producers: {formatList(producers)}")

    flexible_eaters = identify_most_flexible_eaters(food_web)
    print(f"Most Flexible Eaters: {formatList(flexible_eaters)}")

    tastiest = identify_tastiest_organisms(food_web)
    print(f"Tastiest: {formatList(tastiest)}")

    heights = calculate_heights(food_web)
    print("Heights:")
    for species, height in sorted(heights.items()):
        print(f"  {species}: {height}")

if __name__ == "__main__":
    main()