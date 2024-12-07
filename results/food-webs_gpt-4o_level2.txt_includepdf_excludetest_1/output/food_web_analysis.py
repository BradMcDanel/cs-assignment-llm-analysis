import sys
from formatList import formatList

def load_data(file_name):
    """Load the predator-prey data from the specified file."""
    food_web = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                food_web[predator] = prey
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
        sys.exit(1)
    return food_web

def part1_display_predators_and_prey(food_web):
    """Display what each predator eats."""
    print("Predators and Prey:")
    for predator, prey in sorted(food_web.items()):
        formatted_prey = formatList(prey)
        print(f"  {predator} eats {formatted_prey}")

def part2_identify_apex_predators(food_web):
    """Identify the apex predators."""
    prey_set = {prey for preys in food_web.values() for prey in preys}
    apex_predators = [predator for predator in food_web if predator not in prey_set]
    print("Apex Predators:", formatList(apex_predators))

def part3_identify_producers(food_web):
    """Identify the producers."""
    producers = [predator for predator, prey in food_web.items() if len(prey) == 0]
    print("Producers:", formatList(producers))

def part4_identify_most_flexible_eaters(food_web):
    """Identify the most flexible eaters."""
    max_prey_count = max(len(prey) for prey in food_web.values())
    most_flexible_eaters = [predator for predator, prey in food_web.items() if len(prey) == max_prey_count]
    print("Most Flexible Eaters:", formatList(most_flexible_eaters))

def part5_identify_tastiest_organisms(food_web):
    """Identify the tastiest organisms."""
    prey_counts = {}
    for preys in food_web.values():
        for prey in preys:
            if prey in prey_counts:
                prey_counts[prey] += 1
            else:
                prey_counts[prey] = 1
    max_prey_count = max(prey_counts.values())
    tastiest_organisms = [prey for prey, count in prey_counts.items() if count == max_prey_count]
    print("Tastiest:", formatList(tastiest_organisms))

def part6_determine_heights(food_web):
    """Determine the height of each organism in the food web."""
    heights = {organism: 0 for organism in food_web.keys()}
    changed = True
    while changed:
        changed = False
        for predator, preys in food_web.items():
            for prey in preys:
                if heights[predator] <= heights.get(prey, 0):
                    heights[predator] = heights.get(prey, 0) + 1
                    changed = True
    print("Heights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

def main():
    # Check command-line arguments
    if len(sys.argv) > 2:
        print("Error: Too many command line arguments provided.")
        sys.exit(1)
    elif len(sys.argv) == 2:
        file_name = sys.argv[1]
    else:
        file_name = input("Enter the food web file name: ")

    # Load the data
    food_web = load_data(file_name)

    # Perform the analysis
    part1_display_predators_and_prey(food_web)
    part2_identify_apex_predators(food_web)
    part3_identify_producers(food_web)
    part4_identify_most_flexible_eaters(food_web)
    part5_identify_tastiest_organisms(food_web)
    part6_determine_heights(food_web)

if __name__ == "__main__":
    main()