import sys
from formatList import formatList

def read_file(file_name):
    data = {}
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip().split(',')
            predator = line[0]
            prey = line[1:]
            data[predator] = prey
    return data

def part1(data):
    print("Predators and Prey:")
    for predator, prey in sorted(data.items()):
        formatted_prey = formatList(prey)
        print(f"  {predator} eats {formatted_prey}")

def part2(data):
    apex_predators = []
    for predator in data.keys():
        eaten_by_other = False
        for prey_list in data.values():
            if predator in prey_list:
                eaten_by_other = True
                break
        if not eaten_by_other:
            apex_predators.append(predator)
    print("Apex Predators:", formatList(apex_predators))

def part3(data):
    producers = []
    for predator in data.keys():
        if not data[predator]:
            producers.append(predator)
    print("Producers:", formatList(producers))

def part4(data):
    max_eats = max(len(eats) for eats in data.values())
    most_flexible_eaters = [predator for predator, prey in data.items() if len(prey) == max_eats]
    print("Most Flexible Eaters:", formatList(most_flexible_eaters))

def part5(data):
    prey_count = {}
    for prey_list in data.values():
        for prey in prey_list:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values())
    tastiest_organisms = [organism for organism, count in prey_count.items() if count == max_count]
    print("Tastiest Organisms:", formatList(tastiest_organisms))

def part6(data):
    heights = {}
    for organism in data.keys():
        if organism not in heights:
            heights[organism] = 0
        for prey in data[organism]:
            heights[prey] = max(heights.get(prey, 0), heights[organism] + 1)
    
    print("Heights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python food_web_analysis.py <food_web_file>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    try:
        data = read_file(file_name)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        sys.exit(1)

    part1(data)
    part2(data)
    part3(data)
    part4(data)
    part5(data)
    part6(data)

if __name__ == "__main__":
    main()