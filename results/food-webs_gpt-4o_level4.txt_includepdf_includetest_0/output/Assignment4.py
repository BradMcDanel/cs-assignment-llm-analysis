import sys
from collections import defaultdict
from formatList import formatList

def read_food_web(filename):
    try:
        with open(filename, 'r') as file:
            food_web = defaultdict(list)
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                preys = parts[1:]
                food_web[predator].extend(preys)
        return food_web
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)

def print_predators_and_prey(food_web):
    print("Predators and Prey:")
    for predator, preys in sorted(food_web.items()):
        print(f"  {predator} eats {formatList(preys)}")

def find_apex_predators(food_web):
    prey_set = {prey for preys in food_web.values() for prey in preys}
    apex_predators = [predator for predator in food_web if predator not in prey_set]
    print(f"Apex Predators: {formatList(apex_predators)}")

def find_producers(food_web):
    producers = [predator for predator, preys in food_web.items() if not preys]
    print(f"Producers: {formatList(producers)}")

def find_most_flexible_eaters(food_web):
    max_prey_count = max(len(preys) for preys in food_web.values())
    most_flexible_eaters = [predator for predator, preys in food_web.items() if len(preys) == max_prey_count]
    print(f"Most Flexible Eaters: {formatList(most_flexible_eaters)}")

def find_tastiest_organisms(food_web):
    prey_count = defaultdict(int)
    for preys in food_web.values():
        for prey in preys:
            prey_count[prey] += 1
    max_count = max(prey_count.values())
    tastiest_organisms = [prey for prey, count in prey_count.items() if count == max_count]
    print(f"Tastiest: {formatList(tastiest_organisms)}")

def calculate_heights(food_web):
    heights = {organism: 0 for organism in food_web}
    changed = True
    while changed:
        changed = False
        for predator, preys in food_web.items():
            for prey in preys:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    return heights

def print_heights(heights):
    print("Heights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    elif len(sys.argv) == 1:
        filename = input("Please enter the name of the food web file: ")
    else:
        print("Error: Too many command line arguments.")
        sys.exit(1)

    food_web = read_food_web(filename)
    print_predators_and_prey(food_web)
    find_apex_predators(food_web)
    find_producers(food_web)
    find_most_flexible_eaters(food_web)
    find_tastiest_organisms(food_web)
    heights = calculate_heights(food_web)
    print_heights(heights)

if __name__ == "__main__":
    main()