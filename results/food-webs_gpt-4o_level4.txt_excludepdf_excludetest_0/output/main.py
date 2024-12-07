import sys
import os
from format_utils import format_predator_eats

def load_food_web(file_path):
    """Load the predator-prey relationships from the CSV file into a dictionary."""
    food_web = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                food_web[predator] = prey
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        sys.exit(1)
    return food_web

def part1_display_predators_and_prey(food_web):
    """Display all predators and their prey."""
    print("Predators and Prey:")
    for predator in sorted(food_web.keys()):
        prey_list = food_web[predator]
        print("  " + format_predator_eats(predator, prey_list))

def part2_identify_apex_predators(food_web):
    """Identify and display apex predators."""
    apex_predators = set(food_web.keys())
    for prey in food_web.values():
        for organism in prey:
            apex_predators.discard(organism)
    print("Apex Predators:", ", ".join(sorted(apex_predators)))

def part3_identify_producers(food_web):
    """Identify and display producers."""
    producers = set()
    for predator, prey in food_web.items():
        if len(prey) == 0:
            producers.add(predator)
    print("Producers:", ", ".join(sorted(producers)))

def part4_most_flexible_eaters(food_web):
    """Identify and display the most flexible eaters."""
    max_prey_count = 0
    most_flexible = []
    for predator, prey in food_web.items():
        prey_count = len(prey)
        if prey_count > max_prey_count:
            most_flexible = [predator]
            max_prey_count = prey_count
        elif prey_count == max_prey_count:
            most_flexible.append(predator)
    print("Most Flexible Eaters:", ", ".join(sorted(most_flexible)))

def part5_tastiest_organisms(food_web):
    """Identify and display the tastiest organisms."""
    prey_count = {}
    for prey in food_web.values():
        for organism in prey:
            prey_count[organism] = prey_count.get(organism, 0) + 1
    max_count = max(prey_count.values(), default=0)
    tastiest = [organism for organism, count in prey_count.items() if count == max_count]
    print("Tastiest:", ", ".join(sorted(tastiest)))

def part6_determine_heights(food_web):
    """Determine and display the height of each organism in the food web."""
    heights = {organism: 0 for organism in food_web}
    changed = True
    while changed:
        changed = False
        for predator, prey in food_web.items():
            for organism in prey:
                if heights[predator] <= heights.get(organism, 0):
                    heights[predator] = heights.get(organism, 0) + 1
                    changed = True
    print("Heights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    food_web = load_food_web(file_path)
    
    part1_display_predators_and_prey(food_web)
    part2_identify_apex_predators(food_web)
    part3_identify_producers(food_web)
    part4_most_flexible_eaters(food_web)
    part5_tastiest_organisms(food_web)
    part6_determine_heights(food_web)

if __name__ == "__main__":
    main()