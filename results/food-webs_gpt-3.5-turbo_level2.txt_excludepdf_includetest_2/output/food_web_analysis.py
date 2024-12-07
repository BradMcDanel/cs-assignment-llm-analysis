import sys
from formatting import format_output

def read_file(file_name):
    food_web = {}
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            predator, *prey = line.split(',')
            food_web[predator] = prey
    return food_web

def part1(food_web):
    print("Predators and Prey:")
    for predator, prey in sorted(food_web.items()):
        formatted_preys = format_output(prey)
        print(f"{predator} eats {formatted_preys}")

def part2(food_web):
    print("Apex Predators:")
    apex_predators = [predator for predator in food_web if not any(predator in preys for preys in food_web.values())]
    print(format_output(apex_predators))

def part3(food_web):
    print("Producers:")
    producers = [predator for predator, preys in food_web.items() if not preys]
    print(format_output(producers))

def part4(food_web):
    print("Most Flexible Eaters:")
    max_eats = max(len(preys) for preys in food_web.values())
    flexible_eaters = [predator for predator, preys in food_web.items() if len(preys) == max_eats]
    print(format_output(flexible_eaters))

def part5(food_web):
    print("Tastiest:")
    all_prey = [prey for preys in food_web.values() for prey in preys]
    tastiest_organisms = [organism for organism in food_web if all_prey.count(organism) == len(food_web)]
    print(format_output(tastiest_organisms))

def part6(food_web):
    print("Heights:")
    heights = {}
    for organism in food_web:
        heights[organism] = 0

    changed = True
    while changed:
        changed = False
        for predator, preys in food_web.items():
            for prey in preys:
                if heights[predator] <= heights.get(prey, -1):
                    heights[predator] = heights[prey] + 1
                    changed = True

    for organism, height in sorted(heights.items()):
        print(f"{organism}: {height}")

def main(file_name):
    food_web = read_file(file_name)
    part1(food_web)
    part2(food_web)
    part3(food_web)
    part4(food_web)
    part5(food_web)
    part6(food_web)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("Please provide the food web file name as a command line argument.")