import sys
import os
from formatList import formatList

def load_food_web(file_path):
    food_web = {}
    try:
        with open(file_path) as f:
            for line in f:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                food_web[predator] = prey
        return food_web
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def list_predators_and_prey(food_web):
    print("Predators and Prey:")
    for predator in sorted(food_web):
        formatted_prey = formatList(food_web[predator])
        print(f"  {predator} eats {formatted_prey}")

def identify_apex_predators(food_web):
    all_prey = {animal for prey_list in food_web.values() for animal in prey_list}
    apex_predators = [predator for predator in food_web if predator not in all_prey]
    print(f"Apex Predators: {formatList(sorted(apex_predators))}")

def identify_producers(food_web):
    producers = [predator for predator, prey in food_web.items() if len(prey) == 0]
    print(f"Producers: {formatList(sorted(producers))}")

def identify_most_flexible_eaters(food_web):
    max_prey_count = max(len(prey) for prey in food_web.values())
    most_flexible_eaters = [predator for predator, prey in food_web.items() if len(prey) == max_prey_count]
    print(f"Most Flexible Eaters: {formatList(sorted(most_flexible_eaters))}")

def identify_tastiest_organism(food_web):
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            if prey not in prey_count:
                prey_count[prey] = 0
            prey_count[prey] += 1
    max_count = max(prey_count.values())
    tastiest = [organism for organism, count in prey_count.items() if count == max_count]
    print(f"Tastiest: {formatList(sorted(tastiest))}")

def determine_heights(food_web):
    heights = {organism: 0 for organism in food_web}
    changed = True
    while changed:
        changed = False
        for predator, preys in food_web.items():
            for prey in preys:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    print("Heights:")
    for organism in sorted(heights, key=heights.get, reverse=True):
        print(f"  {organism}: {heights[organism]}")

def main():
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    elif len(sys.argv) == 1:
        file_path = input("Please enter the name of the food web file: ")
    else:
        print("Error: Too many command line arguments.")
        sys.exit(1)
    
    food_web = load_food_web(file_path)
    list_predators_and_prey(food_web)
    identify_apex_predators(food_web)
    identify_producers(food_web)
    identify_most_flexible_eaters(food_web)
    identify_tastiest_organism(food_web)
    determine_heights(food_web)

if __name__ == "__main__":
    main()