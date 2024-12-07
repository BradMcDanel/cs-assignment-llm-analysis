def load_food_web(file):
    food_web = {}
    for line in file:
        parts = line.strip().split(',')
        predator = parts[0].strip()
        prey = [p.strip() for p in parts[1:]]
        food_web[predator] = prey
    return food_web

def display_predators_and_prey(food_web):
    for predator, prey in sorted(food_web.items()):
        formatted_prey = ', '.join(prey[:-1]) + (' and ' + prey[-1] if len(prey) > 1 else prey[0])
        print(f"  {predator} eats {formatted_prey}")

def identify_apex_predators(food_web):
    all_prey = set(prey for prey_list in food_web.values() for prey in prey_list)
    return [predator for predator in food_web.keys() if predator not in all_prey]

def identify_producers(food_web):
    return [animal for animal, prey in food_web.items() if not prey]

def identify_most_flexible_eaters(food_web):
    max_prey_count = max(len(prey) for prey in food_web.values())
    return [predator for predator, prey in food_web.items() if len(prey) == max_prey_count]

def identify_tastiest_organisms(food_web):
    prey_count = {}
    for prey_list in food_web.values():
        for prey in prey_list:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    max_count = max(prey_count.values())
    return [organism for organism, count in prey_count.items() if count == max_count]

def determine_organism_heights(food_web):
    heights = {organism: 0 for organism in food_web}
    changed = True

    while changed:
        changed = False
        for predator, prey in food_web.items():
            for p in prey:
                if heights[predator] <= heights[p]:
                    heights[predator] = heights[p] + 1
                    changed = True

    return heights