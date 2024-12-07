import sys

def read_file(file_name):
    """Read the predator-prey file and return a dictionary."""
    food_web = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                food_web[predator] = prey
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        sys.exit(1)
    return food_web

def list_predators_and_prey(food_web):
    """List everything that each predator eats with nice formatting."""
    print("Predators and Prey:")
    for predator, prey_list in sorted(food_web.items()):
        prey_string = ', '.join(prey_list[:-1])
        if prey_list[-1]:
            prey_string += f" and {prey_list[-1]}"
        print(f"  {predator} eats {prey_string}")

def identify_apex_predators(food_web):
    """Identify and return a list of apex predators."""
    all_prey = {prey for prey_list in food_web.values() for prey in prey_list}
    apex_predators = [predator for predator in food_web.keys() if predator not in all_prey]
    print(f"Apex Predators: {', '.join(sorted(apex_predators))}")

def identify_producers(food_web):
    """Identify and return a list of producers (species that do not eat other species)."""
    producers = [species for species, prey_list in food_web.items() if not prey_list]
    print(f"Producers: {', '.join(sorted(producers))}")

def identify_most_flexible_eaters(food_web):
    """Identify the organisms that eat the greatest number of other organisms."""
    max_prey_count = max(len(prey) for prey in food_web.values())
    most_flexible_eaters = [predator for predator, prey in food_web.items() if len(prey) == max_prey_count]
    print(f"Most Flexible Eaters: {', '.join(sorted(most_flexible_eaters))}")

def identify_tastiest_organisms(food_web):
    """Identify the organisms that are eaten by the most different predators."""
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_preyed_count = max(prey_count.values())
    tastiest_organisms = [prey for prey, count in prey_count.items() if count == max_preyed_count]
    print(f"Tastiest: {', '.join(sorted(tastiest_organisms))}")

def determine_heights(food_web):
    """Determine the height of each organism in the food web."""
    heights = {species: 0 for species in food_web.keys()}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in food_web.items():
            for prey in prey_list:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    print("Heights:")
    for species, height in sorted(heights.items()):
        print(f"  {species}: {height}")

def main():
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    else:
        file_name = input("Enter the food web file name: ")
    
    food_web = read_file(file_name)
    list_predators_and_prey(food_web)
    identify_apex_predators(food_web)
    identify_producers(food_web)
    identify_most_flexible_eaters(food_web)
    identify_tastiest_organisms(food_web)
    determine_heights(food_web)

if __name__ == "__main__":
    main()