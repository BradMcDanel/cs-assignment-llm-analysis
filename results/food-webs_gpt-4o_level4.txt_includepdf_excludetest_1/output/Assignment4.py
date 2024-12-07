import sys
import os
from formatList import formatList

def load_food_web(filename):
    food_web = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                food_web[predator] = prey
    except IOError:
        print(f"Error: The file {filename} could not be opened.")
        sys.exit(1)
    return food_web

def part1(food_web):
    print("Predators and Prey:")
    for predator in sorted(food_web.keys()):
        prey_list = formatList(food_web[predator])
        print(f"  {predator} eats {prey_list}")

def part2(food_web):
    all_prey = set(prey for preys in food_web.values() for prey in preys)
    apex_predators = sorted(predator for predator in food_web.keys() if predator not in all_prey)
    print(f"Apex Predators: {formatList(apex_predators)}")

def part3(food_web):
    producers = sorted(predator for predator, preys in food_web.items() if len(preys) == 1 and preys[0] not in food_web)
    print(f"Producers: {formatList(producers)}")

def part4(food_web):
    max_prey_count = max(len(preys) for preys in food_web.values())
    most_flexible_eaters = sorted(predator for predator, preys in food_web.items() if len(preys) == max_prey_count)
    print(f"Most Flexible Eaters: {formatList(most_flexible_eaters)}")

def part5(food_web):
    prey_count = {}
    for preys in food_web.values():
        for prey in preys:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_prey_count = max(prey_count.values())
    tastiest = sorted(prey for prey, count in prey_count.items() if count == max_prey_count)
    print(f"Tastiest: {formatList(tastiest)}")

def calculate_heights(food_web):
    heights = {predator: 0 for predator in food_web.keys()}
    changed = True
    while changed:
        changed = False
        for predator, preys in food_web.items():
            for prey in preys:
                if prey in heights and heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    return heights

def part6(food_web):
    heights = calculate_heights(food_web)
    print("Heights:")
    for predator in sorted(heights.keys()):
        print(f"  {predator}: {heights[predator]}")

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input("Enter the name of the food web file: ")
    
    if not os.path.isfile(filename):
        print(f"Error: The file {filename} does not exist.")
        sys.exit(1)
    
    food_web = load_food_web(filename)
    part1(food_web)
    part2(food_web)
    part3(food_web)
    part4(food_web)
    part5(food_web)
    part6(food_web)

if __name__ == "__main__":
    main()