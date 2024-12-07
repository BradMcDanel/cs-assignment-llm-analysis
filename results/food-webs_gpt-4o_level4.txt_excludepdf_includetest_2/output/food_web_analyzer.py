def load_food_web(filename):
    food_web = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            predator = parts[0]
            prey = parts[1:]
            food_web[predator] = prey
    return food_web

def display_predators_and_prey(food_web):
    print("Predators and Prey:")
    for predator in sorted(food_web):
        prey_list = food_web[predator]
        formatted_prey = format_prey_list(prey_list)
        print(f"  {predator} eats {formatted_prey}")

def format_prey_list(prey_list):
    if len(prey_list) == 1:
        return prey_list[0]
    return ', '.join(prey_list[:-1]) + " and " + prey_list[-1]

def find_apex_predators(food_web):
    all_prey = {prey for prey_list in food_web.values() for prey in prey_list}
    return [predator for predator in food_web if predator not in all_prey]

def find_producers(food_web):
    return [organism for organism in food_web if not food_web[organism]]

def find_most_flexible_eaters(food_web):
    max_prey_count = max(len(prey_list) for prey_list in food_web.values())
    return [predator for predator, prey_list in food_web.items() if len(prey_list) == max_prey_count]

def find_tastiest_organisms(food_web):
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values())
    return [prey for prey, count in prey_count.items() if count == max_count]

def calculate_heights(food_web):
    heights = {organism: 0 for organism in food_web}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in food_web.items():
            for prey in prey_list:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    return heights