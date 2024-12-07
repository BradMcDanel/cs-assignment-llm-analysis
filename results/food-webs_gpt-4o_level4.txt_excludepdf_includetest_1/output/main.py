import sys
import os

def load_data(filename):
    """Load predator-prey relationships from the file into a dictionary."""
    predator_prey = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                predator_prey[predator] = prey
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    return predator_prey

def display_predators_and_prey(predator_prey):
    """Display what each predator eats."""
    print("Predators and Prey:")
    for predator, preys in sorted(predator_prey.items()):
        preys_str = ", ".join(preys[:-1]) + " and " + preys[-1] if len(preys) > 1 else preys[0]
        print(f"  {predator} eats {preys_str}")

def find_apex_predators(predator_prey):
    """Identify apex predators."""
    all_prey = {prey for prey_list in predator_prey.values() for prey in prey_list}
    apex_predators = [predator for predator in predator_prey if predator not in all_prey]
    print("Apex Predators:", ", ".join(apex_predators))

def find_producers(predator_prey):
    """Identify producers."""
    producers = [predator for predator, preys in predator_prey.items() if not preys]
    print("Producers:", ", ".join(producers))

def find_most_flexible_eaters(predator_prey):
    """Identify the most flexible eaters."""
    max_prey_count = max(len(preys) for preys in predator_prey.values())
    flexible_eaters = [predator for predator, preys in predator_prey.items() if len(preys) == max_prey_count]
    print("Most Flexible Eaters:", ", ".join(flexible_eaters))

def find_tastiest_organisms(predator_prey):
    """Identify the tastiest organisms."""
    prey_count = {}
    for preys in predator_prey.values():
        for prey in preys:
            if prey in prey_count:
                prey_count[prey] += 1
            else:
                prey_count[prey] = 1
    max_count = max(prey_count.values())
    tastiest = [prey for prey, count in prey_count.items() if count == max_count]
    print("Tastiest:", ", ".join(tastiest))

def calculate_heights(predator_prey):
    """Determine the height of each organism in the food web."""
    heights = {producer: 0 for producer in predator_prey if not predator_prey[producer]}
    changed = True
    while changed:
        changed = False
        for predator, preys in predator_prey.items():
            if predator not in heights:
                max_height = max(heights.get(prey, 0) for prey in preys)
                if max_height + 1 > heights.get(predator, 0):
                    heights[predator] = max_height + 1
                    changed = True
    print("Heights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

def main():
    if len(sys.argv) < 2:
        filename = input("Enter the food web filename: ")
    elif len(sys.argv) > 2:
        print("Error: Too many command line arguments.")
        sys.exit(1)
    else:
        filename = sys.argv[1]

    predator_prey = load_data(filename)
    display_predators_and_prey(predator_prey)
    find_apex_predators(predator_prey)
    find_producers(predator_prey)
    find_most_flexible_eaters(predator_prey)
    find_tastiest_organisms(predator_prey)
    calculate_heights(predator_prey)

if __name__ == "__main__":
    main()