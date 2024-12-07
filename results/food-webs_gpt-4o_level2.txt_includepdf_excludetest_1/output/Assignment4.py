import sys
import os
from formatList import formatList

def load_food_web(filename):
    try:
        with open(filename, 'r') as file:
            food_web = {}
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0].strip()
                prey = [p.strip() for p in parts[1:]]
                food_web[predator] = prey
        return food_web
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)

def print_predators_and_prey(food_web):
    print("Predators and Prey:")
    for predator in sorted(food_web.keys()):
        print(f"  {predator} eats {formatList(food_web[predator])}")

def identify_apex_predators(food_web):
    prey_set = {prey for preys in food_web.values() for prey in preys}
    apex_predators = sorted(set(food_web.keys()) - prey_set)
    print("Apex Predators:", formatList(apex_predators))

def identify_producers(food_web):
    producers = sorted([predator for predator, preys in food_web.items() if not preys])
    print("Producers:", formatList(producers))

def identify_most_flexible_eaters(food_web):
    max_eats = max(len(preys) for preys in food_web.values())
    most_flexible_eaters = sorted([predator for predator, preys in food_web.items() if len(preys) == max_eats])
    print("Most Flexible Eaters:", formatList(most_flexible_eaters))

def identify_tastiest_organism(food_web):
    prey_count = {}
    for preys in food_web.values():
        for prey in preys:
            if prey in prey_count:
                prey_count[prey] += 1
            else:
                prey_count[prey] = 1
    max_count = max(prey_count.values())
    tastiest = sorted([prey for prey, count in prey_count.items() if count == max_count])
    print("Tastiest:", formatList(tastiest))

def determine_heights(food_web):
    heights = {organism: 0 for organism in food_web}
    changed = True
    while changed:
        changed = False
        for predator in food_web:
            for prey in food_web[predator]:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    print("Heights:")
    for organism in sorted(heights.keys()):
        print(f"  {organism}: {heights[organism]}")

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    elif len(sys.argv) == 1:
        filename = input("Enter the name of the food web file: ")
    else:
        print("Error: Too many command line arguments provided.")
        sys.exit(1)
    
    food_web = load_food_web(filename)
    print_predators_and_prey(food_web)
    identify_apex_predators(food_web)
    identify_producers(food_web)
    identify_most_flexible_eaters(food_web)
    identify_tastiest_organism(food_web)
    determine_heights(food_web)

if __name__ == "__main__":
    main()