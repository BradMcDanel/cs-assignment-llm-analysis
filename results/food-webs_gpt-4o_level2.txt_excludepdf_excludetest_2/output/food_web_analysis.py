import sys

def read_food_web(file_name):
    """Read the predator-prey relationships from a file and return a dictionary representation."""
    try:
        with open(file_name, 'r') as file:
            food_web = {}
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                food_web[predator] = prey
            return food_web
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        sys.exit(1)

def format_prey_list(prey_list):
    """Format the prey list with commas and 'and' for the last item."""
    if len(prey_list) > 1:
        return ', '.join(prey_list[:-1]) + ' and ' + prey_list[-1]
    else:
        return prey_list[0]

def display_predators_and_prey(food_web):
    """Display everything that each predator eats."""
    print("Predators and Prey:")
    for predator, prey in sorted(food_web.items()):
        formatted_prey = format_prey_list(prey)
        print(f"  {predator} eats {formatted_prey}")

def find_apex_predators(food_web):
    """Identify and return a list of apex predators."""
    all_prey = {prey for prey_list in food_web.values() for prey in prey_list}
    apex_predators = [predator for predator in food_web if predator not in all_prey]
    return apex_predators

def display_apex_predators(apex_predators):
    """Display the apex predators."""
    formatted_apex_predators = format_prey_list(apex_predators)
    print(f"Apex Predators: {formatted_apex_predators}")

def find_producers(food_web):
    """Identify and return a list of producers."""
    producers = [organism for organism, prey in food_web.items() if not prey]
    return producers

def display_producers(producers):
    """Display the producers."""
    formatted_producers = format_prey_list(producers)
    print(f"Producers: {formatted_producers}")

def find_most_flexible_eaters(food_web):
    """Identify and return the organism(s) that eat the greatest number of other organisms."""
    max_prey_count = max(len(prey) for prey in food_web.values())
    most_flexible_eaters = [predator for predator, prey in food_web.items() if len(prey) == max_prey_count]
    return most_flexible_eaters

def display_most_flexible_eaters(most_flexible_eaters):
    """Display the most flexible eaters."""
    formatted_flexible_eaters = format_prey_list(most_flexible_eaters)
    print(f"Most Flexible Eaters: {formatted_flexible_eaters}")

def find_tastiest_organisms(food_web):
    """Identify and return the organism(s) that are eaten by the most different organisms."""
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            if prey not in prey_count:
                prey_count[prey] = 0
            prey_count[prey] += 1
    max_count = max(prey_count.values())
    tastiest = [organism for organism, count in prey_count.items() if count == max_count]
    return tastiest

def display_tastiest_organisms(tastiest):
    """Display the tastiest organisms."""
    formatted_tastiest = format_prey_list(tastiest)
    print(f"Tastiest: {formatted_tastiest}")

def calculate_heights(food_web, producers):
    """Calculate and return the height of each organism in the food web."""
    heights = {organism: 0 for organism in food_web}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in food_web.items():
            for prey in prey_list:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    return heights

def display_heights(heights):
    """Display the height of each organism."""
    print("Heights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

def main():
    # Handle command line arguments
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    elif len(sys.argv) == 1:
        file_name = input("Enter the name of the food web file: ")
    else:
        print("Error: Too many command line arguments provided.")
        sys.exit(1)

    # Read the food web from the file
    food_web = read_food_web(file_name)

    # Part 1: Display predators and prey
    display_predators_and_prey(food_web)

    # Part 2: Identify and display apex predators
    apex_predators = find_apex_predators(food_web)
    display_apex_predators(apex_predators)

    # Part 3: Identify and display producers
    producers = find_producers(food_web)
    display_producers(producers)

    # Part 4: Identify and display the most flexible eaters
    most_flexible_eaters = find_most_flexible_eaters(food_web)
    display_most_flexible_eaters(most_flexible_eaters)

    # Part 5: Identify and display the tastiest organisms
    tastiest = find_tastiest_organisms(food_web)
    display_tastiest_organisms(tastiest)

    # Part 6: Determine and display the height of each organism
    heights = calculate_heights(food_web, producers)
    display_heights(heights)

if __name__ == "__main__":
    main()