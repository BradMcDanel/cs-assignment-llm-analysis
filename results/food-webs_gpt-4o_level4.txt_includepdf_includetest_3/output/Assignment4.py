import sys
from formatList import formatList

def load_food_web(filename):
    try:
        with open(filename, 'r') as file:
            food_web = {}
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0].strip()
                prey_list = [prey.strip() for prey in parts[1:]]
                food_web[predator] = prey_list
        return food_web
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)

def display_predators_and_prey(food_web):
    print("Predators and Prey:")
    for predator in sorted(food_web.keys()):
        prey = food_web[predator]
        print(f"  {predator} eats {formatList(prey)}")

def find_apex_predators(food_web):
    all_prey = {prey for preys in food_web.values() for prey in preys}
    apex_predators = [predator for predator in food_web.keys() if predator not in all_prey]
    print(f"Apex Predators: {formatList(apex_predators)}")

def find_producers(food_web):
    producers = [predator for predator, prey in food_web.items() if len(prey) == 0]
    print(f"Producers: {formatList(producers)}")

def find_most_flexible_eaters(food_web):
    max_prey_count = max(len(prey) for prey in food_web.values())
    most_flexible = [predator for predator, prey in food_web.items() if len(prey) == max_prey_count]
    print(f"Most Flexible Eaters: {formatList(most_flexible)}")

def find_tastiest_organisms(food_web):
    prey_count = {}
    for preys in food_web.values():
        for prey in preys:
            if prey in prey_count:
                prey_count[prey] += 1
            else:
                prey_count[prey] = 1
    max_count = max(prey_count.values())
    tastiest = [prey for prey, count in prey_count.items() if count == max_count]
    print(f"Tastiest: {formatList(tastiest)}")

def calculate_heights(food_web):
    heights = {animal: 0 for animal in food_web.keys()}
    changed = True
    while changed:
        changed = False
        for predator, preys in food_web.items():
            for prey in preys:
                if prey in heights and heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    print("Heights:")
    for animal in sorted(heights.keys()):
        print(f"  {animal}: {heights[animal]}")

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    elif len(sys.argv) == 1:
        filename = input("Enter the food web filename: ")
    else:
        print("Error: Too many command line arguments.")
        sys.exit(1)
    
    food_web = load_food_web(filename)
    display_predators_and_prey(food_web)
    find_apex_predators(food_web)
    find_producers(food_web)
    find_most_flexible_eaters(food_web)
    find_tastiest_organisms(food_web)
    calculate_heights(food_web)

if __name__ == "__main__":
    main()