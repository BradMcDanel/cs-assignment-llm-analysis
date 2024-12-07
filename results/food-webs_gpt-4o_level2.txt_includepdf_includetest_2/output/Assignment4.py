import sys
import os

def formatList(data):
    # Handle the case where the list is empty
    if len(data) == 0:
        return "(None)"
    
    # Start with an empty string that we will add items to
    retval = ""

    # Handle all of the items except for the last two
    for i in range(0, len(data) - 2):
        retval = retval + str(data[i]) + ", "

    # Handle the second last item
    if len(data) >= 2:
        retval += str(data[-2]) + " and "

    # Handle the last item
    retval += str(data[-1])

    # Return the result
    return retval

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
        sys.exit(1)
    return food_web

def part1(food_web):
    print("Predators and Prey:")
    for predator, preys in sorted(food_web.items()):
        print(f"  {predator} eats {formatList(preys)}")

def part2(food_web):
    all_prey = set(prey for preys in food_web.values() for prey in preys)
    apex_predators = [predator for predator in food_web if predator not in all_prey]
    print(f"Apex Predators: {formatList(apex_predators)}")

def part3(food_web):
    producers = [predator for predator, preys in food_web.items() if len(preys) == 0]
    print(f"Producers: {formatList(producers)}")

def part4(food_web):
    max_eats = max(len(preys) for preys in food_web.values())
    most_flexible_eaters = [predator for predator, preys in food_web.items() if len(preys) == max_eats]
    print(f"Most Flexible Eaters: {formatList(most_flexible_eaters)}")

def part5(food_web):
    tastiness_count = {}
    for preys in food_web.values():
        for prey in preys:
            if prey in tastiness_count:
                tastiness_count[prey] += 1
            else:
                tastiness_count[prey] = 1
    max_tastiness = max(tastiness_count.values())
    tastiest = [prey for prey, count in tastiness_count.items() if count == max_tastiness]
    print(f"Tastiest: {formatList(tastiest)}")

def part6(food_web):
    heights = {organism: 0 for organism in food_web}
    changed = True
    while changed:
        changed = False
        for predator, preys in food_web.items():
            for prey in preys:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    print("Heights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python Assignment4.py <food_web_file>")
        sys.exit(1)

    filename = sys.argv[1]
    food_web = load_food_web(filename)
    part1(food_web)
    part2(food_web)
    part3(food_web)
    part4(food_web)
    part5(food_web)
    part6(food_web)

if __name__ == "__main__":
    main()