import sys
from formatList import formatList

def read_file(filename):
    # Read the file and store the predator-prey relationships in a dictionary
    relationships = {}
    with open(filename, 'r') as file:
        for line in file:
            line_data = line.strip().split(',')
            predator = line_data[0]
            prey = line_data[1:]
            relationships[predator] = prey
    return relationships

def part1(relationships):
    # List everything that each predator eats
    print("Predators and Prey:")
    for predator, prey in sorted(relationships.items()):
        formatted_prey = formatList(prey)
        print(f"  {predator} eats {formatted_prey}")

def part2(relationships):
    # Identify and display all apex predators
    print("Apex Predators:", end=" ")
    apex_predators = [predator for predator in relationships if predator not in set(sum(relationships.values(), []))]
    print(formatList(apex_predators))

def part3(relationships):
    # Identify and display all producers
    print("Producers:", end=" ")
    producers = [predator for predator, prey in relationships.items() if not prey]
    print(formatList(producers))

def part4(relationships):
    # Identify and display the most flexible eaters
    print("Most Flexible Eaters:", end=" ")
    max_eats = max([len(prey) for prey in relationships.values()])
    flexible_eaters = [predator for predator, prey in relationships.items() if len(prey) == max_eats]
    print(formatList(flexible_eaters))

def part5(relationships):
    # Identify and display the tastiest organism
    print("Tastiest:", end=" ")
    all_prey = sum(relationships.values(), [])
    counter = {organism: all_prey.count(organism) for organism in set(all_prey)}
    max_count = max(counter.values())
    tastiest_organisms = [organism for organism, count in counter.items() if count == max_count]
    print(formatList(tastiest_organisms))

def part6(relationships):
    # Determine the height of each organism in the food web
    heights = {organism: 0 for organism in relationships}
    changed = True
    while changed:
        changed = False
        for predator, prey in relationships.items():
            for p in prey:
                if heights[predator] <= heights.get(p, 0):
                    heights[predator] = heights[p] + 1
                    changed = True
    print("Heights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Please provide the food web file as a command line argument.")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        relationships = read_file(filename)
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

    part1(relationships)
    part2(relationships)
    part3(relationships)
    part4(relationships)
    part5(relationships)
    part6(relationships)