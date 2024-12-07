import sys
from collections import defaultdict

def load_food_web(file_name):
    """Load the predator-prey relationships from a file into a dictionary."""
    food_web = defaultdict(list)
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey_list = parts[1:]
                food_web[predator].extend(prey_list)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        sys.exit(1)
    return food_web

def format_prey_list(prey_list):
    """Format the list of prey with commas and 'and' for display."""
    if len(prey_list) == 1:
        return prey_list[0]
    return ', '.join(prey_list[:-1]) + ' and ' + prey_list[-1]

def display_predators_and_prey(food_web):
    """Display what each predator eats."""
    print("Predators and Prey:")
    for predator in sorted(food_web.keys()):
        formatted_prey = format_prey_list(food_web[predator])
        print(f"  {predator} eats {formatted_prey}")

def identify_apex_predators(food_web):
    """Identify and display all apex predators."""
    all_prey = set(prey for preys in food_web.values() for prey in preys)
    apex_predators = [predator for predator in food_web if predator not in all_prey]
    print("Apex Predators:", ', '.join(apex_predators))

def identify_producers(food_web):
    """Identify and display all producers."""
    producers = [organism for organism in food_web if not food_web[organism]]
    print("Producers:", ' and '.join(producers))

def identify_most_flexible_eaters(food_web):
    """Identify and display the most flexible eaters."""
    max_prey_count = max(len(preys) for preys in food_web.values())
    most_flexible = [predator for predator, preys in food_web.items() if len(preys) == max_prey_count]
    print("Most Flexible Eaters:", ', '.join(most_flexible))

def identify_tastiest_organisms(food_web):
    """Identify and display the tastiest organisms."""
    prey_count = defaultdict(int)
    for preys in food_web.values():
        for prey in preys:
            prey_count[prey] += 1
    max_count = max(prey_count.values())
    tastiest = [prey for prey, count in prey_count.items() if count == max_count]
    print("Tastiest:", ' and '.join(tastiest))

def determine_heights(food_web):
    """Determine and display the height of each organism in the food web."""
    heights = {organism: 0 for organism in food_web}
    changed = True
    while changed:
        changed = False
        for predator, preys in food_web.items():
            for prey in preys:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    print("Heights:")
    for organism in sorted(heights):
        print(f"  {organism}: {heights[organism]}")

def main():
    # Handle command-line arguments
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    elif len(sys.argv) > 2:
        print("Error: Too many command-line arguments provided.")
        sys.exit(1)
    else:
        file_name = input("Enter the name of the food web file: ")

    food_web = load_food_web(file_name)

    # Part 1
    display_predators_and_prey(food_web)

    # Part 2
    identify_apex_predators(food_web)

    # Part 3
    identify_producers(food_web)

    # Part 4
    identify_most_flexible_eaters(food_web)

    # Part 5
    identify_tastiest_organisms(food_web)

    # Part 6
    determine_heights(food_web)

if __name__ == "__main__":
    main()