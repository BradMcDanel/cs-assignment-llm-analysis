def process_food_web(file):
    """Read the food web from the file and return it as a dictionary."""
    food_web = {}
    for line in file:
        parts = line.strip().split(',')
        predator = parts[0]
        prey = parts[1:]
        food_web[predator] = prey
    return food_web

def find_apex_predators(food_web):
    """Return a list of apex predators."""
    prey_set = {prey for prey_list in food_web.values() for prey in prey_list}
    return [predator for predator in food_web if predator not in prey_set]

def find_producers(food_web):
    """Return a list of producers."""
    return [organism for organism, prey in food_web.items() if not prey]

def find_most_flexible_eaters(food_web):
    """Return a list of the most flexible eaters."""
    max_prey_count = max(len(prey) for prey in food_web.values())
    return [predator for predator, prey in food_web.items() if len(prey) == max_prey_count]

def find_tastiest_organisms(food_web):
    """Return a list of the tastiest organisms."""
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            if prey in prey_count:
                prey_count[prey] += 1
            else:
                prey_count[prey] = 1
    max_count = max(prey_count.values())
    return [prey for prey, count in prey_count.items() if count == max_count]

def determine_heights(food_web):
    """Determine the height of each organism in the food web."""
    height = {organism: 0 for organism in food_web}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in food_web.items():
            for prey in prey_list:
                if height[predator] <= height[prey]:
                    height[predator] = height[prey] + 1
                    changed = True
    return height