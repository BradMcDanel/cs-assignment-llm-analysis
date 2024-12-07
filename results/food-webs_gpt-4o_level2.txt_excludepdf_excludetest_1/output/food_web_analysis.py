def read_food_web(filename):
    """Reads the food web data from a CSV file and returns a dictionary."""
    food_web = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                food_web[predator] = prey
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    return food_web

def display_predators_and_prey(food_web):
    """Displays each predator and its prey in a formatted manner."""
    print("Predators and Prey:")
    for predator in sorted(food_web.keys()):
        prey_list = food_web[predator]
        formatted_prey = ', '.join(prey_list[:-1]) + " and " + prey_list[-1] if len(prey_list) > 1 else prey_list[0]
        print(f"  {predator} eats {formatted_prey}")

def find_apex_predators(food_web):
    """Identifies and returns the apex predators in the food web."""
    all_prey = {prey for preys in food_web.values() for prey in preys}
    apex_predators = [predator for predator in food_web if predator not in all_prey]
    return apex_predators

def find_producers(food_web):
    """Identifies and returns the producers in the food web."""
    producers = [predator for predator, prey in food_web.items() if not prey]
    return producers

def find_most_flexible_eaters(food_web):
    """Identifies and returns the most flexible eaters in the food web."""
    max_prey_count = max(len(prey) for prey in food_web.values())
    most_flexible_eaters = [predator for predator, prey in food_web.items() if len(prey) == max_prey_count]
    return most_flexible_eaters

def find_tastiest_organisms(food_web):
    """Identifies and returns the tastiest organisms in the food web."""
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            if prey in prey_count:
                prey_count[prey] += 1
            else:
                prey_count[prey] = 1
    max_predators_count = max(prey_count.values())
    tastiest_organisms = [prey for prey, count in prey_count.items() if count == max_predators_count]
    return tastiest_organisms

def calculate_heights(food_web, producers):
    """Calculates and returns the height of each organism in the food web."""
    heights = {organism: 0 for organism in food_web}
    changed = True
    while changed:
        changed = False
        for predator, prey in food_web.items():
            for p in prey:
                if heights[predator] <= heights[p]:
                    heights[predator] = heights[p] + 1
                    changed = True
    return heights

def main():
    import sys

    if len(sys.argv) != 2:
        print("Usage: python food_web_analysis.py <filename>")
        return
    
    filename = sys.argv[1]
    food_web = read_food_web(filename)
    if food_web is None:
        return

    display_predators_and_prey(food_web)

    apex_predators = find_apex_predators(food_web)
    print("\nApex Predators:", ", ".join(apex_predators))

    producers = find_producers(food_web)
    print("\nProducers:", ", ".join(producers) if producers else "(None)")

    most_flexible_eaters = find_most_flexible_eaters(food_web)
    print("\nMost Flexible Eaters:", ", ".join(most_flexible_eaters))

    tastiest_organisms = find_tastiest_organisms(food_web)
    print("\nTastiest:", ", ".join(tastiest_organisms))

    heights = calculate_heights(food_web, producers)
    print("\nHeights:")
    for organism in sorted(heights.keys()):
        print(f"  {organism}: {heights[organism]}")

if __name__ == "__main__":
    main()