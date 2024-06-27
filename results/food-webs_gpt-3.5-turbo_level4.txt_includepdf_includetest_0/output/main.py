import sys

# Function to load predator-prey relationships from a file into a dictionary
def load_food_web_data(file_name):
    data = {}
    with open(file_name, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            predator = parts[0]
            prey = parts[1:]
            data[predator] = prey
    return data

# Function to list everything each predator eats
def list_predator_eats(data):
    for predator, prey in data.items():
        print(predator + " eats " + formatList(prey))

# Function to identify apex predators
def identify_apex_predators(data):
    apex_predators = []
    for predator in data.keys():
        eaten_by_anyone = False
        for prey_list in data.values():
            if predator in prey_list:
                eaten_by_anyone = True
                break
        if not eaten_by_anyone:
            apex_predators.append(predator)
    return apex_predators

# Function to identify producers
def identify_producers(data):
    producers = []
    for predator in data.keys():
        eaten_by_anyone = False
        for prey_list in data.values():
            if predator in prey_list:
                eaten_by_anyone = True
                break
        if not eaten_by_anyone:
            producers.append(predator)
    return producers

# Function to identify the most flexible eaters
def identify_flexible_eaters(data):
    max_eaten = max([len(prey) for prey in data.values()])
    flexible_eaters = [predator for predator, prey in data.items() if len(prey) == max_eaten]
    return flexible_eaters

# Function to identify the tastiest organism
def identify_tastiest(data):
    eaten_by = {}
    for prey_list in data.values():
        for prey in prey_list:
            eaten_by[prey] = eaten_by.get(prey, 0) + 1
    max_eaten_count = max(eaten_by.values())
    tastiest = [organism for organism, count in eaten_by.items() if count == max_eaten_count]
    return tastiest

# Function to determine the height of each organism in the food web
def determine_heights(data):
    heights = {}
    for organism in data.keys():
        heights[organism] = 0
    changed = True
    while changed:
        changed = False
        for predator, prey in data.items():
            for p in prey:
                if heights[predator] <= heights.get(p, -1):
                    heights[predator] = heights[p] + 1
                    changed = True
    return heights

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <food_web_file>")
    else:
        file_name = sys.argv[1]
        try:
            food_web_data = load_food_web_data(file_name)
            print("Predators and Prey:")
            list_predator_eats(food_web_data)
            print("Apex Predators:", identify_apex_predators(food_web_data))
            print("Producers:", identify_producers(food_web_data))
            print("Most Flexible Eaters:", identify_flexible_eaters(food_web_data))
            print("Tastiest:", identify_tastiest(food_web_data))
            print("Heights:")
            heights = determine_heights(food_web_data)
            for organism, height in heights.items():
                print("  " + organism + ": " + str(height))
        except FileNotFoundError:
            print("Error: File not found.")