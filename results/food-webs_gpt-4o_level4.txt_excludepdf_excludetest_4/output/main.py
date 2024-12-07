import sys
import os

def load_data(filename):
    """Load predator-prey relationships from a CSV file into a dictionary."""
    relationships = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                relationships[predator] = prey
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    return relationships

def part_1(relationships):
    """Display what each predator eats with proper formatting."""
    print("Predators and Prey:")
    for predator, prey_list in sorted(relationships.items()):
        formatted_prey = ', '.join(prey_list[:-1]) + " and " + prey_list[-1]
        print(f"  {predator} eats {formatted_prey}")

def part_2(relationships):
    """Identify and display apex predators."""
    all_prey = {prey for preys in relationships.values() for prey in preys}
    apex_predators = [predator for predator in relationships if predator not in all_prey]
    print("Apex Predators: " + ', '.join(apex_predators))

def part_3(relationships):
    """Identify and display producers."""
    producers = [organism for organism in relationships if not relationships[organism]]
    print("Producers: " + ' and '.join(producers))

def part_4(relationships):
    """Identify and display the most flexible eaters."""
    max_prey_count = max(len(prey) for prey in relationships.values())
    flexible_eaters = [predator for predator, prey in relationships.items() if len(prey) == max_prey_count]
    print("Most Flexible Eaters: " + ', '.join(flexible_eaters))

def part_5(relationships):
    """Identify and display the tastiest organisms."""
    prey_count = {}
    for prey_list in relationships.values():
        for prey in prey_list:
            if prey in prey_count:
                prey_count[prey] += 1
            else:
                prey_count[prey] = 1
    max_preys = max(prey_count.values())
    tastiest_organisms = [prey for prey, count in prey_count.items() if count == max_preys]
    print("Tastiest: " + ' and '.join(tastiest_organisms))

def part_6(relationships):
    """Determine and display the height of each organism."""
    heights = {organism: 0 for organism in relationships}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in relationships.items():
            for prey in prey_list:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    print("Heights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

def main():
    if len(sys.argv) != 2:
        filename = input("Enter the filename: ") if len(sys.argv) == 1 else sys.exit("Error: Please provide exactly one filename.")
    else:
        filename = sys.argv[1]
    
    relationships = load_data(filename)
    part_1(relationships)
    part_2(relationships)
    part_3(relationships)
    part_4(relationships)
    part_5(relationships)
    part_6(relationships)

if __name__ == "__main__":
    main()