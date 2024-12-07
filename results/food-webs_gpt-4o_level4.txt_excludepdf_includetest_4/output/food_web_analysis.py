import sys

def load_food_web(file_name):
    """Load the predator-prey relationships from the file and store them in a dictionary."""
    try:
        with open(file_name, 'r') as file:
            food_web = {}
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey_list = parts[1:]
                food_web[predator] = prey_list
            return food_web
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        sys.exit(1)

def display_predators_and_prey(food_web):
    """Display each predator and what they eat."""
    print("Predators and Prey:")
    for predator, prey_list in sorted(food_web.items()):
        formatted_prey = ', '.join(prey_list[:-1]) + (' and ' if len(prey_list) > 1 else '') + prey_list[-1]
        print(f"  {predator} eats {formatted_prey}")

def find_apex_predators(food_web):
    """Identify and return a list of apex predators."""
    all_prey = set(prey for preys in food_web.values() for prey in preys)
    apex_predators = [predator for predator in food_web if predator not in all_prey]
    return apex_predators

def find_producers(food_web):
    """Identify and return a list of producers."""
    producers = [predator for predator, prey_list in food_web.items() if not prey_list]
    return producers

def find_most_flexible_eaters(food_web):
    """Identify and return the most flexible eaters."""
    max_prey_count = max(len(prey_list) for prey_list in food_web.values())
    most_flexible_eaters = [predator for predator, prey_list in food_web.items() if len(prey_list) == max_prey_count]
    return most_flexible_eaters

def find_tastiest_organisms(food_web):
    """Identify and return the tastiest organisms."""
    prey_counter = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            if prey in prey_counter:
                prey_counter[prey] += 1
            else:
                prey_counter[prey] = 1
    max_eaten_count = max(prey_counter.values())
    tastiest_organisms = [prey for prey, count in prey_counter.items() if count == max_eaten_count]
    return tastiest_organisms

def determine_heights(food_web):
    """Determine the height of each organism and return a dictionary with heights."""
    heights = {organism: 0 for organism in food_web}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in food_web.items():
            max_prey_height = max((heights[prey] for prey in prey_list if prey in heights), default=0)
            if heights[predator] <= max_prey_height:
                heights[predator] = max_prey_height + 1
                changed = True
    return heights

def main():
    if len(sys.argv) != 2:
        print("Usage: python food_web_analysis.py <filename>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    food_web = load_food_web(file_name)
    
    display_predators_and_prey(food_web)
    
    apex_predators = find_apex_predators(food_web)
    print("\nApex Predators:", ', '.join(apex_predators))
    
    producers = find_producers(food_web)
    print("Producers:", ' and '.join(producers) if producers else "(None)")
    
    most_flexible_eaters = find_most_flexible_eaters(food_web)
    print("Most Flexible Eaters:", ', '.join(most_flexible_eaters))
    
    tastiest_organisms = find_tastiest_organisms(food_web)
    print("Tastiest:", ' and '.join(tastiest_organisms))
    
    heights = determine_heights(food_web)
    print("Heights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

if __name__ == "__main__":
    main()