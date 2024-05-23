def load_food_web(filename):
    food_web = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            predator = parts[0]
            prey = parts[1:]
            food_web[predator] = prey
    return food_web

def list_predators_and_prey(food_web):
    for predator, prey_list in sorted(food_web.items()):
        if len(prey_list) == 1:
            print(f"  {predator} eats {prey_list[0]}")
        else:
            print(f"  {predator} eats {', '.join(prey_list[:-1])} and {prey_list[-1]}")

def find_apex_predators(food_web):
    all_prey = {prey for prey_list in food_web.values() for prey in prey_list}
    apex_predators = [predator for predator in food_web.keys() if predator not in all_prey]
    return apex_predators

def find_producers(food_web):
    producers = [predator for predator, prey_list in food_web.items() if not prey_list]
    return producers

def find_most_flexible_eaters(food_web):
    max_eats = max(len(prey) for prey in food_web.values())
    most_flexible = [predator for predator, prey in food_web.items() if len(prey) == max_eats]
    return most_flexible

def find_tastiest_organisms(food_web):
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            if prey not in prey_count:
                prey_count[prey] = 0
            prey_count[prey] += 1
    max_count = max(prey_count.values())
    tastiest = [organism for organism, count in prey_count.items() if count == max_count]
    return tastiest

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