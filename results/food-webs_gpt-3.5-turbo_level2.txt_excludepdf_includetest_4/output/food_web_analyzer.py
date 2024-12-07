import sys

def read_food_web(file_name):
    food_web = {}
    with open(file_name, 'r') as file:
        for line in file:
            predator, *prey = line.strip().split(',')
            food_web[predator] = prey
    return food_web

def list_predators_and_prey(food_web):
    for predator, prey_list in food_web.items():
        formatted_prey = ', '.join(prey_list[:-1]) + ' and ' + prey_list[-1]
        print(f'{predator} eats {formatted_prey}')

def identify_apex_predators(food_web):
    apex_predators = [predator for predator in food_web.keys() if predator not in [prey for predators in food_web.values() for prey in predators]]
    print("Apex Predators:", ', '.join(apex_predators))

def identify_producers(food_web):
    producers = [predator for predator in food_web.keys() if not food_web[predator]]
    print("Producers:", ', '.join(producers))

def identify_most_flexible_eaters(food_web):
    max_eaten_count = max(len(prey_list) for prey_list in food_web.values())
    most_flexible_eaters = [predator for predator, prey_list in food_web.items() if len(prey_list) == max_eaten_count]
    print("Most Flexible Eaters:", ', '.join(most_flexible_eaters))

def identify_tastiest_organisms(food_web):
    all_prey = [prey for prey_list in food_web.values() for prey in prey_list]
    prey_count = {prey: all_prey.count(prey) for prey in set(all_prey)}
    max_prey_count = max(prey_count.values())
    tastiest_organisms = [prey for prey, count in prey_count.items() if count == max_prey_count]
    print("Tastiest Organisms:", ', '.join(tastiest_organisms))

def determine_heights(food_web):
    heights = {}
    for predator in food_web.keys():
        if predator not in heights:
            calculate_height(predator, food_web, heights)
    for organism, height in heights.items():
        print(f'{organism}: {height}')

def calculate_height(organism, food_web, heights):
    if organism not in food_web or not food_web[organism]:
        heights[organism] = 0
        return 0
    prey_heights = [calculate_height(prey, food_web, heights) for prey in food_web[organism]]
    heights[organism] = 1 + max(prey_heights)

def main():
    if len(sys.argv) != 2:
        print("Error: Provide the filename as a command line argument.")
        sys.exit(1)
    
    file_name = sys.argv[1]
    food_web = read_food_web(file_name)
    
    print("Predators and Prey:")
    list_predators_and_prey(food_web)
    
    identify_apex_predators(food_web)
    
    identify_producers(food_web)
    
    identify_most_flexible_eaters(food_web)
    
    identify_tastiest_organisms(food_web)
    
    print("Heights:")
    determine_heights(food_web)

if __name__ == "__main__":
    main()