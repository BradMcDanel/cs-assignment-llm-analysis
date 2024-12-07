import sys

def read_food_web_file(filename):
    try:
        with open(filename, 'r') as file:
            food_web = {}
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey_list = parts[1:]
                food_web[predator] = prey_list
            return food_web
    except FileNotFoundError:
        print("Error: The file was not found.")
        sys.exit(1)

def display_predators_and_prey(food_web):
    print("Predators and Prey:")
    for predator in sorted(food_web.keys()):
        prey = food_web[predator]
        print(f"  {predator} eats " + formatList(prey))

def identify_apex_predators(food_web):
    prey_set = {prey for preys in food_web.values() for prey in preys}
    apex_predators = [predator for predator in food_web.keys() if predator not in prey_set]
    print("\nApex Predators: " + formatList(apex_predators))

def identify_producers(food_web):
    producers = [predator for predator, prey in food_web.items() if not prey]
    print("\nProducers: " + formatList(producers))

def identify_most_flexible_eaters(food_web):
    max_eats = max(len(prey) for prey in food_web.values())
    flexible_eaters = [predator for predator, prey in food_web.items() if len(prey) == max_eats]
    print("\nMost Flexible Eaters: " + formatList(flexible_eaters))

def identify_tastiest_organism(food_web):
    eaten_count = {}
    for preys in food_web.values():
        for prey in preys:
            eaten_count[prey] = eaten_count.get(prey, 0) + 1
    max_eaten = max(eaten_count.values())
    tastiest = [organism for organism, count in eaten_count.items() if count == max_eaten]
    print("\nTastiest: " + formatList(tastiest))

def determine_heights(food_web):
    heights = {organism: 0 for organism in food_web.keys()}
    changed = True
    while changed:
        changed = False
        for predator, preys in food_web.items():
            for prey in preys:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    print("\nHeights:")
    for organism in sorted(heights.keys()):
        print(f"  {organism}: {heights[organism]}")

def main():
    # Handle command line arguments
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    elif len(sys.argv) > 2:
        print("Error: Too many command line arguments.")
        sys.exit(1)
    else:
        filename = input("Enter the food web file name: ")

    # Load the food web data
    food_web = read_food_web_file(filename)

    # Part 1: Display predators and prey
    display_predators_and_prey(food_web)

    # Part 2: Identify apex predators
    identify_apex_predators(food_web)

    # Part 3: Identify producers
    identify_producers(food_web)

    # Part 4: Identify the most flexible eaters
    identify_most_flexible_eaters(food_web)

    # Part 5: Identify the tastiest organism
    identify_tastiest_organism(food_web)

    # Part 6: Determine heights of organisms
    determine_heights(food_web)

if __name__ == "__main__":
    main()