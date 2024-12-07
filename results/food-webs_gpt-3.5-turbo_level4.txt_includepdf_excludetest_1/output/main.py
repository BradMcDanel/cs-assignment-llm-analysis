import sys

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit()

def create_food_web_dict(lines):
    food_web_dict = {}
    for line in lines:
        line = line.strip().split(',')
        predator = line[0]
        prey = line[1:]
        food_web_dict[predator] = prey
    return food_web_dict

def part_one(food_web_dict):
    for predator, prey in sorted(food_web_dict.items()):
        print(predator, "eats", formatList(prey))

def part_two(food_web_dict):
    apex_predators = [predator for predator in food_web_dict if predator not in set([prey for predators in food_web_dict.values() for prey in predators])]
    print("Apex Predators:", formatList(apex_predators))

def part_three(food_web_dict):
    producers = [predator for predator, prey in food_web_dict.items() if not prey]
    print("Producers:", formatList(producers))

def part_four(food_web_dict):
    max_eats = max([len(prey) for prey in food_web_dict.values()])
    most_flexible_eaters = [predator for predator, prey in food_web_dict.items() if len(prey) == max_eats]
    print("Most Flexible Eaters:", formatList(most_flexible_eaters))

def part_five(food_web_dict):
    prey_count = {}
    for prey_list in food_web_dict.values():
        for prey in prey_list:
            prey_count[prey] = prey_count.get(prey, 0) + 1
    tastiest_organisms = [organism for organism, count in prey_count.items() if count == max(prey_count.values())]
    print("Tastiest Organisms:", formatList(tastiest_organisms))

def part_six(food_web_dict):
    heights = {predator: 0 for predator in food_web_dict}
    changed = True
    while changed:
        changed = False
        for predator, prey in food_web_dict.items():
            for p in prey:
                if heights[predator] <= heights.get(p, -1):
                    heights[predator] = heights[p] + 1
                    changed = True
    print("Heights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else input("Enter the filename: ")
    lines = read_file(filename)
    food_web_dict = create_food_web_dict(lines)
    
    part_one(food_web_dict)
    part_two(food_web_dict)
    part_three(food_web_dict)
    part_four(food_web_dict)
    part_five(food_web_dict)
    part_six(food_web_dict)