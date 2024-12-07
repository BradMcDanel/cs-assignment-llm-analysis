import sys
import os
from formatList import formatList

def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = {}
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                data[predator] = prey
            return data
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        sys.exit(1)

def display_predators_and_prey(data):
    print("Predators and Prey:")
    for predator in sorted(data.keys()):
        prey = formatList(data[predator])
        print(f"  {predator} eats {prey}")

def identify_apex_predators(data):
    all_prey = {animal for prey_list in data.values() for animal in prey_list}
    apex_predators = [predator for predator in data if predator not in all_prey]
    print(f"Apex Predators: {formatList(sorted(apex_predators))}")

def identify_producers(data):
    producers = [predator for predator, prey in data.items() if len(prey) == 1 and prey[0].islower()]
    print(f"Producers: {formatList(sorted(producers))}")

def identify_flexible_eaters(data):
    max_prey_count = max(len(prey) for prey in data.values())
    flexible_eaters = [predator for predator, prey in data.items() if len(prey) == max_prey_count]
    print(f"Most Flexible Eaters: {formatList(sorted(flexible_eaters))}")

def identify_tastiest_organisms(data):
    prey_counter = {prey: 0 for prey_list in data.values() for prey in prey_list}
    for prey_list in data.values():
        for prey in prey_list:
            prey_counter[prey] += 1
    max_eaten_count = max(prey_counter.values())
    tastiest_organisms = [prey for prey, count in prey_counter.items() if count == max_eaten_count]
    print(f"Tastiest: {formatList(sorted(tastiest_organisms))}")

def determine_heights(data):
    heights = {animal: 0 for animal in data.keys()}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in data.items():
            for prey in prey_list:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    print("Heights:")
    for animal in sorted(heights.keys()):
        print(f"  {animal}: {heights[animal]}")

def main():
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    elif len(sys.argv) == 1:
        file_name = input("Enter the name of the file: ")
    else:
        print("Error: Too many command line arguments.")
        sys.exit(1)
    
    data = load_data(file_name)

    display_predators_and_prey(data)
    identify_apex_predators(data)
    identify_producers(data)
    identify_flexible_eaters(data)
    identify_tastiest_organisms(data)
    determine_heights(data)

if __name__ == "__main__":
    main()