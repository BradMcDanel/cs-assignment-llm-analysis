import sys
from format_list import formatList

def read_food_web(filename):
    food_web = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    predator = parts[0].strip()
                    preys = [prey.strip() for prey in parts[1:]]
                    food_web[predator] = preys
        return food_web
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
        sys.exit(1)

def find_apex_predators(food_web):
    prey_list = [prey for preys in food_web.values() for prey in preys]
    return [predator for predator in food_web.keys() if predator not in prey_list]

def find_producers(food_web):
    return list(set([prey for preys in food_web.values() for prey in preys if prey not in food_web.keys()]))

def find_flexible_eaters(food_web):
    max_prey_count = max(len(preys) for preys in food_web.values())
    return [predator for predator, preys in food_web.items() if len(preys) == max_prey_count]

def find_tastiest(food_web):
    prey_count = {}
    for preys in food_web.values():
        for prey in preys:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values())
    return [prey for prey, count in prey_count.items() if count == max_count]

def calculate_heights(food_web):
    heights = {predator: 0 for predator in food_web}
    changed = True
    while changed:
        changed = False
        for predator, preys in food_web.items():
            for prey in preys:
                if heights[predator] <= heights.get(prey, 0):
                    heights[predator] = heights.get(prey, 0) + 1
                    changed = True
    return heights

def main():
    filename = sys.argv[1] if len(sys.argv) == 2 else input("Enter the name of the food web file: ")
    food_web = read_food_web(filename)
    
    # Part 1: Display predator-prey relationships
    print("Predators and Prey:")
    for predator, preys in food_web.items():
        print(f"  {predator} eats {formatList(preys)}")
    
    # Part 2: Apex Predators
    apex_predators = find_apex_predators(food_web)
    print("\nApex Predators:", formatList(apex_predators))
    
    # Part 3: Producers
    producers = find_producers(food_web)
    print("\nProducers:", formatList(producers))
    
    # Part 4: Most Flexible Eaters
    flexible_eaters = find_flexible_eaters(food_web)
    print("\nMost Flexible Eaters:", formatList(flexible_eaters))
    
    # Part 5: Tastiest Organism
    tastiest = find_tastiest(food_web)
    print("\nTastiest:", formatList(tastiest))
    
    # Part 6: Heights
    heights = calculate_heights(food_web)
    print("\nHeights:")
    for organism, height in sorted(heights.items(), key=lambda x: x[1], reverse=True):
        print(f"  {organism}: {height}")

if __name__ == "__main__":
    main()