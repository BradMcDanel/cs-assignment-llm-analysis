import sys

def load_food_web(filename):
    """
    Load the predator-prey relationships from the file into a dictionary.
    Each key is a predator and the value is a list of its prey.
    """
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
        print(f"Error: The file {filename} does not exist.")
        sys.exit(1)

def part1_predators_and_prey(food_web):
    """
    Print each predator and its prey using the formatList function for nice formatting.
    """
    from formatList import formatList

    print("Predators and Prey:")
    for predator, prey_list in sorted(food_web.items()):
        formatted_prey = formatList(prey_list)
        print(f"  {predator} eats {formatted_prey}")

def part2_apex_predators(food_web):
    """
    Identify and print the apex predators, which are not preyed upon by any other animal.
    """
    prey_set = {prey for prey_list in food_web.values() for prey in prey_list}
    apex_predators = [predator for predator in food_web if predator not in prey_set]

    from formatList import formatList
    formatted_apex = formatList(apex_predators)
    print(f"Apex Predators: {formatted_apex}")

def part3_producers(food_web):
    """
    Identify and print the producers, which do not eat any other species.
    """
    producers = [predator for predator, prey_list in food_web.items() if len(prey_list) == 0]

    from formatList import formatList
    formatted_producers = formatList(producers)
    print(f"Producers: {formatted_producers}")

def part4_most_flexible_eaters(food_web):
    """
    Identify and print the most flexible eaters, which eat the greatest number of organisms.
    """
    max_eaten = max(len(prey_list) for prey_list in food_web.values())
    flexible_eaters = [predator for predator, prey_list in food_web.items() if len(prey_list) == max_eaten]

    from formatList import formatList
    formatted_flexible = formatList(flexible_eaters)
    print(f"Most Flexible Eaters: {formatted_flexible}")

def part5_tastiest_organisms(food_web):
    """
    Identify and print the tastiest organisms, which are preyed upon by the most different species.
    """
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            if prey in prey_count:
                prey_count[prey] += 1
            else:
                prey_count[prey] = 1

    max_count = max(prey_count.values())
    tastiest = [prey for prey, count in prey_count.items() if count == max_count]

    from formatList import formatList
    formatted_tastiest = formatList(tastiest)
    print(f"Tastiest: {formatted_tastiest}")

def part6_heights(food_web):
    """
    Calculate and print the height of each organism in the food web.
    """
    # Initialize heights with 0
    heights = {organism: 0 for organism in food_web}

    # Set changed to true to start the loop
    changed = True
    while changed:
        changed = False
        for predator, prey_list in food_web.items():
            for prey in prey_list:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True

    print("Heights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

def main():
    # Check command line arguments
    if len(sys.argv) < 2:
        filename = input("Enter the name of the food web file: ")
    elif len(sys.argv) > 2:
        print("Error: Too many command line arguments.")
        sys.exit(1)
    else:
        filename = sys.argv[1]

    # Load the food web data
    food_web = load_food_web(filename)

    # Perform each part of the analysis
    part1_predators_and_prey(food_web)
    part2_apex_predators(food_web)
    part3_producers(food_web)
    part4_most_flexible_eaters(food_web)
    part5_tastiest_organisms(food_web)
    part6_heights(food_web)

if __name__ == "__main__":
    main()