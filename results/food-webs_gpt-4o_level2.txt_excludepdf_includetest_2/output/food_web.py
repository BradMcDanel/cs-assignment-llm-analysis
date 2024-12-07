import sys

def read_food_web(filename):
    """Reads the food web file and returns a dictionary mapping predators to their prey."""
    food_web = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey_list = parts[1:]
                food_web[predator] = prey_list
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    return food_web

def format_prey_list(prey_list):
    """Formats a list of prey into a string with commas and 'and' for readability."""
    if len(prey_list) == 1:
        return prey_list[0]
    return ', '.join(prey_list[:-1]) + ' and ' + prey_list[-1]

def part1_display_predators_and_prey(food_web):
    """Displays what each predator eats."""
    print("Predators and Prey:")
    for predator in sorted(food_web.keys()):
        prey_list = food_web[predator]
        prey_str = format_prey_list(prey_list)
        print(f"  {predator} eats {prey_str}")

def part2_find_apex_predators(food_web):
    """Finds and displays apex predators."""
    all_prey = set(prey for prey_list in food_web.values() for prey in prey_list)
    apex_predators = [predator for predator in food_web if predator not in all_prey]
    print(f"Apex Predators: {', '.join(sorted(apex_predators))}")

def part3_find_producers(food_web):
    """Finds and displays producers."""
    producers = [predator for predator, prey_list in food_web.items() if not prey_list]
    print(f"Producers: {', '.join(sorted(producers))}")

def part4_find_most_flexible_eaters(food_web):
    """Finds and displays the most flexible eaters."""
    max_prey_count = max(len(prey_list) for prey_list in food_web.values())
    most_flexible_eaters = [predator for predator, prey_list in food_web.items() if len(prey_list) == max_prey_count]
    print(f"Most Flexible Eaters: {', '.join(sorted(most_flexible_eaters))}")

def part5_find_tastiest_organisms(food_web):
    """Finds and displays the tastiest organisms."""
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            if prey not in prey_count:
                prey_count[prey] = 0
            prey_count[prey] += 1
    max_preyed_count = max(prey_count.values())
    tastiest_organisms = [prey for prey, count in prey_count.items() if count == max_preyed_count]
    print(f"Tastiest: {', '.join(sorted(tastiest_organisms))}")

def part6_calculate_heights(food_web):
    """Calculates and displays the height of each organism."""
    heights = {organism: 0 for organism in food_web}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in food_web.items():
            for prey in prey_list:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    print("Heights:")
    for organism in sorted(heights):
        print(f"  {organism}: {heights[organism]}")

def main():
    if len(sys.argv) < 2:
        filename = input("Enter the food web file name: ")
    elif len(sys.argv) > 2:
        print("Error: Too many command line arguments provided.")
        sys.exit(1)
    else:
        filename = sys.argv[1]

    food_web = read_food_web(filename)
    
    part1_display_predators_and_prey(food_web)
    part2_find_apex_predators(food_web)
    part3_find_producers(food_web)
    part4_find_most_flexible_eaters(food_web)
    part5_find_tastiest_organisms(food_web)
    part6_calculate_heights(food_web)

if __name__ == "__main__":
    main()