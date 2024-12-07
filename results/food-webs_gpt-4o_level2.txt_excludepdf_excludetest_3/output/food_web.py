import sys

def load_food_web(filename):
    try:
        with open(filename, 'r') as file:
            food_web = {}
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                food_web[predator] = prey
            return food_web
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

def display_predators_and_prey(food_web):
    print("Predators and Prey:")
    for predator, prey_list in sorted(food_web.items()):
        formatted_prey = format_prey_list(prey_list)
        print(f"  {predator} eats {formatted_prey}")

def format_prey_list(prey_list):
    if len(prey_list) == 1:
        return prey_list[0]
    else:
        return ', '.join(prey_list[:-1]) + ' and ' + prey_list[-1]

def identify_apex_predators(food_web):
    all_prey = set(prey for prey_list in food_web.values() for prey in prey_list)
    apex_predators = [predator for predator in food_web.keys() if predator not in all_prey]
    print(f"Apex Predators: {', '.join(apex_predators)}")

def identify_producers(food_web):
    producers = [predator for predator, prey_list in food_web.items() if not prey_list]
    print(f"Producers: {', '.join(producers)}")

def identify_most_flexible_eaters(food_web):
    max_prey_count = max(len(prey_list) for prey_list in food_web.values())
    most_flexible_eaters = [predator for predator, prey_list in food_web.items() if len(prey_list) == max_prey_count]
    print(f"Most Flexible Eaters: {', '.join(most_flexible_eaters)}")

def identify_tastiest_organisms(food_web):
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            if prey in prey_count:
                prey_count[prey] += 1
            else:
                prey_count[prey] = 1
    max_eaten_count = max(prey_count.values())
    tastiest_organisms = [prey for prey, count in prey_count.items() if count == max_eaten_count]
    print(f"Tastiest: {', '.join(tastiest_organisms)}")

def determine_heights(food_web):
    heights = {animal: 0 for animal in food_web}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in food_web.items():
            for prey in prey_list:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True

    print("Heights:")
    for animal, height in sorted(heights.items()):
        print(f"  {animal}: {height}")

def main():
    if len(sys.argv) < 2:
        filename = input("Enter the name of the file: ")
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print("Error: Too many command line arguments provided.")
        sys.exit(1)
    
    food_web = load_food_web(filename)
    display_predators_and_prey(food_web)
    identify_apex_predators(food_web)
    identify_producers(food_web)
    identify_most_flexible_eaters(food_web)
    identify_tastiest_organisms(food_web)
    determine_heights(food_web)

if __name__ == "__main__":
    main()