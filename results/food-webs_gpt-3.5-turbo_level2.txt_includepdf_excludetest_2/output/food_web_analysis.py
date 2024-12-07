import sys
from formatList import formatList

def read_data(filename):
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().split(',')
            predator = line[0]
            prey = line[1:]
            data[predator] = prey
    return data

def part1(data):
    print("Predators and Prey:")
    for predator, prey_list in sorted(data.items()):
        formatted_prey = formatList(prey_list)
        print(f"  {predator} eats {formatted_prey}")

def part2(data):
    print("Apex Predators:", formatList([predator for predator in data if all(predator not in values for values in data.values())]))

def part3(data):
    print("Producers:", formatList([predator for predator, prey_list in data.items() if not prey_list]))

def part4(data):
    max_eats = max(len(prey_list) for prey_list in data.values())
    most_flexible_eaters = [predator for predator, prey_list in data.items() if len(prey_list) == max_eats]
    print("Most Flexible Eaters:", formatList(most_flexible_eaters))

def part5(data):
    all_prey = [prey for prey_list in data.values() for prey in prey_list]
    tastiest_organisms = [organism for organism in set(all_prey) if all(organism in prey_list for prey_list in data.values())]
    print("Tastiest Organisms:", formatList(tastiest_organisms))

def part6(data):
    heights = {predator: 0 for predator in data}
    changed = True
    while changed:
        changed = False
        for animal, preys in data.items():
            for prey in preys:
                if heights[animal] <= heights.get(prey, -1):
                    heights[animal] = heights[prey] + 1
                    changed = True
    print("Heights:")
    for animal, height in sorted(heights.items()):
        print(f"  {animal}: {height}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python food_web_analysis.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        data = read_data(filename)
    except FileNotFoundError:
        print("File not found!")
        sys.exit(1)
    
    part1(data)
    part2(data)
    part3(data)
    part4(data)
    part5(data)
    part6(data)

if __name__ == "__main__":
    main()