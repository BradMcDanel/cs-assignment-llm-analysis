import sys
from formatList import formatList

def read_file(file_name):
    relationships = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                predator = data[0]
                prey = data[1:]
                relationships[predator] = prey
    except FileNotFoundError:
        print("File not found. Exiting...")
        sys.exit()
    return relationships

def part1(relationships):
    print("Predators and Prey:")
    for predator, prey in sorted(relationships.items()):
        formatted_prey = formatList(prey)
        print(f"  {predator} eats {formatted_prey}")

def find_apex_predators(relationships):
    predators = set(relationships.keys())
    eaten = set()
    for prey in relationships.values():
        eaten.update(prey)
    apex_predators = predators - eaten
    print("Apex Predators:", formatList(sorted(apex_predators)))

def find_producers(relationships):
    producers = set(relationships.keys()) - set(sum(relationships.values(), []))
    print("Producers:", formatList(sorted(producers)))

def find_most_flexible_eaters(relationships):
    max_eaten = max(len(prey) for prey in relationships.values())
    most_flexible_eaters = [predator for predator, prey in relationships.items() if len(prey) == max_eaten]
    print("Most Flexible Eaters:", formatList(most_flexible_eaters))

def find_tastiest_organisms(relationships):
    prey_count = {}
    for prey_list in relationships.values():
        for prey in prey_list:
            if prey in prey_count:
                prey_count[prey] += 1
            else:
                prey_count[prey] = 1
    max_count = max(prey_count.values())
    tastiest_organisms = [organism for organism, count in prey_count.items() if count == max_count]
    print("Tastiest Organisms:", formatList(tastiest_organisms))

def calculate_heights(relationships):
    heights = {predator: 0 for predator in relationships.keys()}
    changed = True
    while changed:
        changed = False
        for predator, prey in relationships.items():
            for animal in prey:
                if heights[animal] <= heights[predator]:
                    heights[animal] = heights[predator] + 1
                    changed = True
    print("Heights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python food_web_analyzer.py <file_name>")
        sys.exit()
    file_name = sys.argv[1]
    relationships = read_file(file_name)
    part1(relationships)
    find_apex_predators(relationships)
    find_producers(relationships)
    find_most_flexible_eaters(relationships)
    find_tastiest_organisms(relationships)
    calculate_heights(relationships)

if __name__ == "__main__":
    main()