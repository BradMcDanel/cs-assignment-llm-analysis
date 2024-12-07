import sys

def read_food_web_data(file_name):
    food_web_data = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                predator, *preys = line.strip().split(',')
                food_web_data[predator] = preys
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    return food_web_data

def list_predator_preys(food_web_data):
    for predator, preys in food_web_data.items():
        formatted_preys = ', '.join(preys[:-1]) + ' and ' + preys[-1] if len(preys) > 1 else preys[0]
        print(f"{predator} eats {formatted_preys}")

def identify_apex_predators(food_web_data):
    apex_predators = [predator for predator in food_web_data if predator not in set(sum(food_web_data.values(), []))]
    print("Apex Predators:", ', '.join(apex_predators))

def identify_producers(food_web_data):
    producers = [predator for predator, preys in food_web_data.items() if not preys]
    print("Producers:", ', '.join(producers))

def identify_most_flexible_eaters(food_web_data):
    max_eats = max(len(preys) for preys in food_web_data.values())
    most_flexible_eaters = [predator for predator, preys in food_web_data.items() if len(preys) == max_eats]
    print("Most Flexible Eaters:", ', '.join(most_flexible_eaters))

def identify_tastiest_organisms(food_web_data):
    prey_counts = {prey: sum(prey in preys for preys in food_web_data.values()) for prey in set(sum(food_web_data.values(), [] )}
    max_count = max(prey_counts.values())
    tastiest_organisms = [prey for prey, count in prey_counts.items() if count == max_count]
    print("Tastiest Organisms:", ', '.join(tastiest_organisms))

def determine_heights(food_web_data):
    heights = {predator: 0 for predator in food_web_data}
    changed = True
    while changed:
        changed = False
        for predator, preys in food_web_data.items():
            for prey in preys:
                if heights[predator] <= heights.get(prey, -1):
                    heights[predator] = heights[prey] + 1
                    changed = True
    for predator, height in heights.items():
        print(f"{predator}: {height}")

def main():
    if len(sys.argv) > 2:
        print("Error: Too many command line arguments.")
        sys.exit(1)
    elif len(sys.argv) == 2:
        file_name = sys.argv[1]
    else:
        file_name = input("Enter the name of the file: ")

    food_web_data = read_food_web_data(file_name)

    print("Predators and Prey:")
    list_predator_preys(food_web_data)

    identify_apex_predators(food_web_data)
    identify_producers(food_web_data)
    identify_most_flexible_eaters(food_web_data)
    identify_tastiest_organisms(food_web_data)
    determine_heights(food_web_data)

if __name__ == "__main__":
    main()