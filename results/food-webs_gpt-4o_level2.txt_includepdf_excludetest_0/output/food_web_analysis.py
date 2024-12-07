import sys
import os
from formatList import formatList

def load_food_web(filename):
    food_web = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0].strip()
                prey_list = [prey.strip() for prey in parts[1:]]
                food_web[predator] = prey_list
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)
    return food_web

def print_predators_and_prey(food_web):
    print("Predators and Prey:")
    for predator in sorted(food_web.keys()):
        print(f"  {predator} eats {formatList(food_web[predator])}")

def find_apex_predators(food_web):
    all_prey = {prey for prey_list in food_web.values() for prey in prey_list}
    apex_predators = [predator for predator in food_web.keys() if predator not in all_prey]
    return apex_predators

def find_producers(food_web):
    producers = [predator for predator, prey_list in food_web.items() if len(prey_list) == 1 and prey_list[0] in food_web]
    return producers

def find_most_flexible_eaters(food_web):
    max_prey_count = max(len(prey_list) for prey_list in food_web.values())
    most_flexible_eaters = [predator for predator, prey_list in food_web.items() if len(prey_list) == max_prey_count]
    return most_flexible_eaters

def find_tastiest_organisms(food_web):
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values())
    tastiest_organisms = [prey for prey, count in prey_count.items() if count == max_count]
    return tastiest_organisms

def calculate_heights(food_web):
    heights = {producer: 0 for producer in find_producers(food_web)}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in food_web.items():
            max_prey_height = max(heights.get(prey, 0) for prey in prey_list)
            if heights.get(predator, 0) <= max_prey_height:
                heights[predator] = max_prey_height + 1
                changed = True
    return heights

def main():
    if len(sys.argv) > 2:
        print("Error: Too many command line arguments provided.")
        sys.exit(1)
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input("Enter the name of the food web file: ")

    food_web = load_food_web(filename)
    print_predators_and_prey(food_web)
    
    apex_predators = find_apex_predators(food_web)
    print(f"Apex Predators: {formatList(apex_predators)}")
    
    producers = find_producers(food_web)
    print(f"Producers: {formatList(producers)}")
    
    most_flexible_eaters = find_most_flexible_eaters(food_web)
    print(f"Most Flexible Eaters: {formatList(most_flexible_eaters)}")
    
    tastiest_organisms = find_tastiest_organisms(food_web)
    print(f"Tastiest: {formatList(tastiest_organisms)}")
    
    heights = calculate_heights(food_web)
    print("Heights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

if __name__ == "__main__":
    main()