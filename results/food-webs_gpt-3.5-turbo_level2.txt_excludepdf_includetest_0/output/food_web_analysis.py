import sys
import csv
from food_web_formatting import format_output

def load_data(file_name):
    data = {}
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            predator = row[0]
            prey = row[1:]
            data[predator] = prey
    return data

def list_predators_and_prey(data):
    for predator, prey_list in data.items():
        formatted_prey = format_output(prey_list)
        print(predator + " eats " + formatted_prey)

def identify_apex_predators(data):
    predators = set(data.keys())
    prey = set()
    for prey_list in data.values():
        prey.update(prey_list)
    apex_predators = predators - prey
    print("Apex Predators:", format_output(list(apex_predators)))

def identify_producers(data):
    producers = set(data.keys()) - set([predator for prey_list in data.values() for predator in prey_list])
    print("Producers:", format_output(list(producers)))

def identify_most_flexible_eaters(data):
    max_eats = max(len(prey_list) for prey_list in data.values())
    most_flexible_eaters = [predator for predator, prey_list in data.items() if len(prey_list) == max_eats]
    print("Most Flexible Eaters:", format_output(most_flexible_eaters))

def identify_tastiest_organisms(data):
    prey_count = {}
    for prey_list in data.values():
        for prey in prey_list:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values())
    tastiest = [prey for prey, count in prey_count.items() if count == max_count]
    print("Tastiest:", format_output(tastiest))

def calculate_heights(data):
    heights = {predator: 0 for predator in data.keys()}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in data.items():
            for prey in prey_list:
                if heights[predator] <= heights.get(prey, 0):
                    heights[predator] = heights[prey] + 1
                    changed = True
    for predator, height in heights.items():
        print(predator + ":", height)

def main():
    if len(sys.argv) != 2:
        print("Error: Please provide the food web file name as a command line argument.")
        sys.exit(1)
    
    file_name = sys.argv[1]
    try:
        data = load_data(file_name)
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    
    print("Predators and Prey:")
    list_predators_and_prey(data)
    
    identify_apex_predators(data)
    identify_producers(data)
    identify_most_flexible_eaters(data)
    identify_tastiest_organisms(data)
    print("Heights:")
    calculate_heights(data)

if __name__ == "__main__":
    main()