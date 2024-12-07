def load_food_web(filename):
    food_web = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                food_web[predator] = prey
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        exit(1)
    return food_web

def get_apex_predators(food_web):
    prey_set = set(prey for prey_list in food_web.values() for prey in prey_list)
    return [predator for predator in food_web.keys() if predator not in prey_set]

def get_producers(food_web):
    return [predator for predator, prey_list in food_web.items() if not prey_list]

def get_most_flexible_eaters(food_web):
    max_prey_count = max(len(prey_list) for prey_list in food_web.values())
    return [predator for predator, prey_list in food_web.items() if len(prey_list) == max_prey_count]

def get_tastiest_organisms(food_web):
    count_map = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            if prey in count_map:
                count_map[prey] += 1
            else:
                count_map[prey] = 1
    max_count = max(count_map.values())
    return [prey for prey, count in count_map.items() if count == max_count]

def calculate_heights(food_web):
    heights = {animal: 0 for animal in food_web.keys()}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in food_web.items():
            for prey in prey_list:
                if prey in heights and heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    return heights