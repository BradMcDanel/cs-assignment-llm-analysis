import sys

def read_food_web(filename):
    """Read the food web from the specified file and return it as a dictionary."""
    food_web = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                food_web[predator] = prey
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    return food_web

def part1_display_predators_and_prey(food_web):
    """Display what each predator eats."""
    print("Predators and Prey:")
    for predator, prey in sorted(food_web.items()):
        formatted_prey = ", ".join(prey[:-1]) + (" and " + prey[-1] if len(prey) > 1 else prey[0])
        print(f"  {predator} eats {formatted_prey}")

def part2_identify_apex_predators(food_web):
    """Identify and display apex predators."""
    all_prey = set(prey for preys in food_web.values() for prey in preys)
    apex_predators = [predator for predator in food_web if predator not in all_prey]
    print("Apex Predators:", ", ".join(apex_predators))

def part3_identify_producers(food_web):
    """Identify and display producers."""
    producers = [species for species, preys in food_web.items() if not preys]
    print("Producers:", " and ".join(producers))

def part4_identify_most_flexible_eaters(food_web):
    """Identify and display the most flexible eaters."""
    max_prey_count = max(len(preys) for preys in food_web.values())
    most_flexible_eaters = [predator for predator, preys in food_web.items() if len(preys) == max_prey_count]
    print("Most Flexible Eaters:", ", ".join(most_flexible_eaters))

def part5_identify_tastiest_organisms(food_web):
    """Identify and display the tastiest organisms."""
    prey_count = {}
    for preys in food_web.values():
        for prey in preys:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values(), default=0)
    tastiest_organisms = [prey for prey, count in prey_count.items() if count == max_count]
    print("Tastiest:", " and ".join(tastiest_organisms))

def part6_determine_heights(food_web):
    """Determine and display the height of each organism."""
    heights = {species: 0 for species in food_web}
    changed = True
    while changed:
        changed = False
        for predator, preys in food_web.items():
            for prey in preys:
                if heights[predator] <= heights.get(prey, 0):
                    heights[predator] = heights.get(prey, 0) + 1
                    changed = True
    print("Heights:")
    for species, height in sorted(heights.items()):
        print(f"  {species}: {height}")

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    elif len(sys.argv) < 2:
        filename = input("Enter the file name: ")
    else:
        print("Error: Too many command line arguments. Please provide only the filename.")
        sys.exit(1)

    food_web = read_food_web(filename)
    part1_display_predators_and_prey(food_web)
    part2_identify_apex_predators(food_web)
    part3_identify_producers(food_web)
    part4_identify_most_flexible_eaters(food_web)
    part5_identify_tastiest_organisms(food_web)
    part6_determine_heights(food_web)

if __name__ == "__main__":
    main()