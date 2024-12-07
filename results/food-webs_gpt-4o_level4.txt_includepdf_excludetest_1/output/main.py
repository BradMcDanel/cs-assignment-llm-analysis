import sys
from formatList import formatList

def load_data(file_name):
    """Load the predator-prey data from a CSV file into a dictionary."""
    predator_prey = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0].strip()
                prey = [item.strip() for item in parts[1:]]
                predator_prey[predator] = prey
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        sys.exit(1)
    return predator_prey

def display_predators_and_prey(predator_prey):
    """Displays what each predator eats in a formatted way."""
    print("Predators and Prey:")
    for predator in sorted(predator_prey.keys()):
        prey_list = formatList(predator_prey[predator])
        print(f"  {predator} eats {prey_list}")

def identify_apex_predators(predator_prey):
    """Identify and print apex predators."""
    all_prey = set()
    for prey in predator_prey.values():
        all_prey.update(prey)
    apex_predators = [pred for pred in predator_prey if pred not in all_prey]
    print(f"Apex Predators: {formatList(apex_predators)}")

def identify_producers(predator_prey):
    """Identify and print producers."""
    producers = [pred for pred, prey in predator_prey.items() if not prey]
    print(f"Producers: {formatList(producers)}")

def identify_most_flexible_eaters(predator_prey):
    """Identify and print the most flexible eaters."""
    max_prey_count = max(len(prey) for prey in predator_prey.values())
    flexible_eaters = [pred for pred, prey in predator_prey.items() if len(prey) == max_prey_count]
    print(f"Most Flexible Eaters: {formatList(flexible_eaters)}")

def identify_tastiest_organisms(predator_prey):
    """Identify and print the tastiest organisms."""
    prey_count = {}
    for prey_list in predator_prey.values():
        for prey in prey_list:
            if prey in prey_count:
                prey_count[prey] += 1
            else:
                prey_count[prey] = 1
    max_eaten_count = max(prey_count.values())
    tastiest = [prey for prey, count in prey_count.items() if count == max_eaten_count]
    print(f"Tastiest: {formatList(tastiest)}")

def determine_heights(predator_prey):
    """Determine and print the height of each organism in the food web."""
    heights = {organism: 0 for organism in predator_prey}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in predator_prey.items():
            for prey in prey_list:
                if heights[predator] <= heights.get(prey, 0):
                    heights[predator] = heights.get(prey, 0) + 1
                    changed = True
    print("Heights:")
    for organism in sorted(heights.keys()):
        print(f"  {organism}: {heights[organism]}")

def main():
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    elif len(sys.argv) == 1:
        file_name = input("Enter the food web file name: ")
    else:
        print("Error: Provide exactly one file name as a command line argument.")
        sys.exit(1)

    predator_prey = load_data(file_name)
    display_predators_and_prey(predator_prey)
    identify_apex_predators(predator_prey)
    identify_producers(predator_prey)
    identify_most_flexible_eaters(predator_prey)
    identify_tastiest_organisms(predator_prey)
    determine_heights(predator_prey)

if __name__ == "__main__":
    main()