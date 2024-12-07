import sys
import csv
from formatting_module import format_eats_relationship

def read_food_web_data(file_name):
    food_web = {}
    
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            predator = row[0]
            prey = row[1:]
            food_web[predator] = prey
    
    return food_web

def list_predator_prey_relationships(food_web):
    for predator, prey_list in food_web.items():
        formatted_relationship = format_eats_relationship(predator, prey_list)
        print(formatted_relationship)

def identify_apex_predators(food_web):
    apex_predators = [predator for predator in food_web if all(predator not in prey_list for prey_list in food_web.values())]
    print("Apex Predators:", ", ".join(apex_predators))

def identify_producers(food_web):
    producers = [organism for organism in food_web if not any(organism in prey_list for prey_list in food_web.values())]
    print("Producers:", ", ".join(producers))

def identify_most_flexible_eaters(food_web):
    max_eaten_count = max(len(prey_list) for prey_list in food_web.values())
    most_flexible_eaters = [predator for predator, prey_list in food_web.items() if len(prey_list) == max_eaten_count]
    print("Most Flexible Eaters:", ", ".join(most_flexible_eaters))

def identify_tastiest_organisms(food_web):
    prey_counts = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            prey_counts[prey] = prey_counts.get(prey, 0) + 1
    
    max_count = max(prey_counts.values())
    tastiest_organisms = [organism for organism, count in prey_counts.items() if count == max_count]
    print("Tastiest Organisms:", ", ".join(tastiest_organisms))

def determine_heights(food_web):
    heights = {organism: 0 for organism in food_web}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in food_web.items():
            for prey in prey_list:
                if heights[predator] <= heights.get(prey, -1):
                    heights[predator] = heights[prey] + 1
                    changed = True
    
    for organism, height in heights.items():
        print(f"{organism}: {height}")

def main():
    file_name = sys.argv[1] if len(sys.argv) > 1 else input("Enter the name of the food web file: ")
    
    try:
        food_web = read_food_web_data(file_name)
        print("Predators and Prey:")
        list_predator_prey_relationships(food_web)
        print()
        identify_apex_predators(food_web)
        print()
        identify_producers(food_web)
        print()
        identify_most_flexible_eaters(food_web)
        print()
        identify_tastiest_organisms(food_web)
        print()
        print("Heights:")
        determine_heights(food_web)
    except FileNotFoundError:
        print("Error: File not found.")

if __name__ == "__main__":
    main()