import sys
from formatList import formatList

def read_file(filename):
    # Read the contents of the file and store the predator-prey relationships in a dictionary
    predator_prey_dict = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip().split(',')
                predator = line[0]
                prey = line[1:]
                predator_prey_dict[predator] = prey
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit()
    
    return predator_prey_dict

def part1(predator_prey_dict):
    print("Predators and Prey:")
    for predator, prey in sorted(predator_prey_dict.items()):
        formatted_prey = formatList(prey)
        print(f"  {predator} eats {formatted_prey}")

def part2(predator_prey_dict):
    apex_predators = [predator for predator in predator_prey_dict if predator not in set(sum(predator_prey_dict.values(), []))]
    print("Apex Predators:", formatList(apex_predators))

def part3(predator_prey_dict):
    producers = [predator for predator, prey in predator_prey_dict.items() if not prey]
    print("Producers:", formatList(producers))

def part4(predator_prey_dict):
    max_eaten_count = max(len(prey) for prey in predator_prey_dict.values())
    most_flexible_eaters = [predator for predator, prey in predator_prey_dict.items() if len(prey) == max_eaten_count]
    print("Most Flexible Eaters:", formatList(most_flexible_eaters))

def part5(predator_prey_dict):
    all_prey = sum(predator_prey_dict.values(), [])
    tastiest_organisms = [organism for organism in set(all_prey) if all_prey.count(organism) == len(predator_prey_dict)]
    print("Tastiest:", formatList(tastiest_organisms))

def part6(predator_prey_dict):
    heights = {organism: 0 for organism in predator_prey_dict}
    changed = True
    while changed:
        changed = False
        for animal, prey in predator_prey_dict.items():
            for p in prey:
                if heights[animal] <= heights.get(p, -1):
                    heights[animal] = heights[p] + 1
                    changed = True
    
    print("Heights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

def main():
    if len(sys.argv) != 2:
        print("Error: Please provide the filename as a command line argument.")
        sys.exit()

    filename = sys.argv[1]
    predator_prey_dict = read_file(filename)

    part1(predator_prey_dict)
    part2(predator_prey_dict)
    part3(predator_prey_dict)
    part4(predator_prey_dict)
    part5(predator_prey_dict)
    part6(predator_prey_dict)

if __name__ == "__main__":
    main()