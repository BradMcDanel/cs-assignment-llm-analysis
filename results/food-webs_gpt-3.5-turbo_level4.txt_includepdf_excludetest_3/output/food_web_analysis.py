import sys

### Part 1: What do the Predators Eat? ###
def get_predator_prey_relationships(filename):
    relationships = {}
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            predator = data[0]
            prey = data[1:]
            relationships[predator] = prey
    return relationships

def part_1(relationships):
    print("Predators and Prey:")
    for predator, prey in sorted(relationships.items()):
        formatted_prey = formatList(prey)
        print(f"  {predator} eats {formatted_prey}")

### Part 2: Identify the Apex Predators ###
def part_2(relationships):
    print("Apex Predators:", end=' ')
    apex_predators = [predator for predator in relationships if all(predator not in value for value in relationships.values())]
    print(formatList(apex_predators))

### Part 3: Identify the Producers ###
def part_3(relationships):
    print("Producers:", end=' ')
    producers = [predator for predator in relationships if not relationships[predator]]
    print(formatList(producers))

### Part 4: Identify the Most Flexible Eaters ###
def part_4(relationships):
    print("Most Flexible Eaters:", end=' ')
    max_eaten = max(len(value) for value in relationships.values())
    flexible_eaters = [predator for predator, prey in relationships.items() if len(prey) == max_eaten]
    print(formatList(flexible_eaters))

### Part 5: The Tastiest Organism ###
def part_5(relationships):
    print("Tastiest Organisms:", end=' ')
    max_eaters = max(len(value) for value in relationships.values())
    tastiest_organisms = [organism for organism in relationships if len(relationships[organism]) == max_eaters]
    print(formatList(tastiest_organisms))

### Part 6: Determine the Height of Each Organism in the Food Web ###
def part_6(relationships):
    print("Heights:")
    heights = {}
    for organism in relationships:
        if not relationships[organism]:
            heights[organism] = 0

    changed = True
    while changed:
        changed = False
        for predator, prey in relationships.items():
            for p in prey:
                if heights[p] >= heights[predator]:
                    heights[predator] = heights[p] + 1
                    changed = True

    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Please provide the filename as a command line argument.")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        relationships = get_predator_prey_relationships(filename)
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

    part_1(relationships)
    part_2(relationships)
    part_3(relationships)
    part_4(relationships)
    part_5(relationships)
    part_6(relationships)