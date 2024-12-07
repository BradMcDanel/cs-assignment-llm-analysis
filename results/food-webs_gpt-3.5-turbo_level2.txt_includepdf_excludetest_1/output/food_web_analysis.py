import sys
from formatList import formatList

def read_file(filename):
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().split(',')
            data[line[0]] = line[1:]
    return data

def part1(data):
    print("Predators and Prey:")
    for predator, prey in sorted(data.items()):
        formatted_prey = formatList(prey)
        print(f"  {predator} eats {formatted_prey}")

def part2(data):
    apex_predators = []
    for predator in data.keys():
        eaten = False
        for prey_list in data.values():
            if predator in prey_list:
                eaten = True
                break
        if not eaten:
            apex_predators.append(predator)
    print("Apex Predators:", formatList(apex_predators))

def part3(data):
    producers = []
    for predator, prey in data.items():
        if not prey:
            producers.append(predator)
    print("Producers:", formatList(producers))

def part4(data):
    max_eater_count = max(len(prey) for prey in data.values())
    most_flexible_eaters = [predator for predator, prey in data.items() if len(prey) == max_eater_count]
    print("Most Flexible Eaters:", formatList(most_flexible_eaters))

def part5(data):
    eaten_by_count = {}
    for prey in set(p for prey_list in data.values() for p in prey):
        eaten_by_count[prey] = sum(1 for predator in data.keys() if prey in data[predator])
    max_eaten_by_count = max(eaten_by_count.values())
    tastiest_organisms = [prey for prey, count in eaten_by_count.items() if count == max_eaten_by_count]
    print("Tastiest Organisms:", formatList(tastiest_organisms))

def part6(data):
    heights = {organism: 0 for organism in data}
    changed = True
    while changed:
        changed = False
        for predator, prey in data.items():
            for animal in prey:
                if heights[animal] >= heights[predator]:
                    heights[predator] = heights[animal] + 1
                    changed = True
    print("Heights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

def main():
    if len(sys.argv) != 2:
        print("Please provide the filename as a command line argument.")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        data = read_file(filename)
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)

    part1(data)
    part2(data)
    part3(data)
    part4(data)
    part5(data)
    part6(data)

if __name__ == "__main__":
    main()