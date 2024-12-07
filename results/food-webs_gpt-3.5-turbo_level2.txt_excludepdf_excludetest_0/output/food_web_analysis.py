import sys
import csv
from formatting_module import format_output

def read_food_web(file_name):
    food_web = {}
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            predator = line[0]
            prey = line[1:]
            food_web[predator] = prey
    return food_web

def part_1(food_web):
    print("Predators and Prey:")
    for predator, prey in sorted(food_web.items()):
        formatted_preys = format_output(prey)
        print(f"{predator} eats {formatted_preys}")

def part_2(food_web):
    print("Apex Predators:")
    apex_predators = [predator for predator in food_web.keys() if predator not in set(sum(food_web.values(), []))]
    for apex_predator in apex_predators:
        print(apex_predator, end=' ')
    print()

def part_3(food_web):
    print("Producers:")
    producers = [predator for predator, prey in food_web.items() if not prey]
    for producer in producers:
        print(producer, end=' ')
    print()

def part_4(food_web):
    print("Most Flexible Eaters:")
    max_eaten_count = max(len(prey) for prey in food_web.values())
    flexible_eaters = [predator for predator, prey in food_web.items() if len(prey) == max_eaten_count]
    for eater in flexible_eaters:
        print(eater, end=' ')
    print()

def part_5(food_web):
    print("Tastiest Organisms:")
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values())
    tastiest_organisms = [prey for prey, count in prey_count.items() if count == max_count]
    for organism in tastiest_organisms:
        print(organism, end=' ')
    print()

def part_6(food_web):
    print("Heights:")
    heights = {}
    for predator in food_web.keys():
        heights[predator] = 0
    changed = True
    while changed:
        changed = False
        for predator, prey in food_web.items():
            for p in prey:
                if heights[predator] <= heights.get(p, -1):
                    heights[predator] = heights[p] + 1
                    changed = True
    for predator, height in heights.items():
        print(f"{predator}: {height}")

def main(file_name):
    food_web = read_food_web(file_name)
    part_1(food_web)
    part_2(food_web)
    part_3(food_web)
    part_4(food_web)
    part_5(food_web)
    part_6(food_web)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    else:
        file_name = input("Enter the name of the food web file: ")
    main(file_name)