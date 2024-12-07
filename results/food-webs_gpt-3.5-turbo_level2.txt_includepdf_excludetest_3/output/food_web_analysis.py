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
        print("Error: File not found.")
        sys.exit()
    
    return relationships

def part1(relationships):
    print("Predators and Prey:")
    for predator, prey in sorted(relationships.items()):
        formatted_prey = formatList(prey)
        print(f"  {predator} eats {formatted_prey}")

def part2(relationships):
    print("Apex Predators:", formatList([predator for predator in relationships if all(predator not in values for values in relationships.values())]))

def part3(relationships):
    print("Producers:", formatList([predator for predator, prey in relationships.items() if not prey]))

def part4(relationships):
    max_eat_count = max(len(prey) for prey in relationships.values())
    most_flexible_eaters = [predator for predator, prey in relationships.items() if len(prey) == max_eat_count]
    print("Most Flexible Eaters:", formatList(most_flexible_eaters))

def part5(relationships):
    all_prey = [prey for pred_prey in relationships.values() for prey in pred_prey]
    tastiest_organisms = [organism for organism in set(all_prey) if all(organism in pred_prey for pred_prey in relationships.values())]
    print("Tastiest Organisms:", formatList(tastiest_organisms))

def part6(relationships):
    heights = {predator: 0 for predator in relationships}
    changed = True
    while changed:
        changed = False
        for predator, prey in relationships.items():
            for p in prey:
                if heights[predator] <= heights.get(p, -1):
                    heights[predator] = heights[p] + 1
                    changed = True
    
    print("Heights:")
    for predator, height in sorted(heights.items()):
        print(f"  {predator}: {height}")

def main():
    if len(sys.argv) != 2:
        print("Error: Please provide the file name as a command line argument.")
        sys.exit()
    
    file_name = sys.argv[1]
    relationships = read_file(file_name)
    
    part1(relationships)
    part2(relationships)
    part3(relationships)
    part4(relationships)
    part5(relationships)
    part6(relationships)

if __name__ == "__main__":
    main()