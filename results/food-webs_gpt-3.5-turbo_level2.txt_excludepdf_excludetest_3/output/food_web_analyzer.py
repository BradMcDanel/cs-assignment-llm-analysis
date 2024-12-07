import sys

def read_data(filename):
    # Read the predator-prey relationships from the file and store them in a dictionary
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            predator, *prey = line.strip().split(',')
            data[predator] = prey
    return data

def list_predator_eats(data):
    for predator, prey_list in sorted(data.items()):
        print(predator, "eats", ", ".join(prey_list[:-1]), "and", prey_list[-1])

def identify_apex_predators(data):
    apex_predators = [predator for predator in data if not any(predator in prey_list for prey_list in data.values())]
    print("Apex Predators:", ", ".join(apex_predators))

def identify_producers(data):
    producers = [predator for predator, prey_list in data.items() if not prey_list]
    print("Producers:", ", ".join(producers))

def identify_most_flexible_eaters(data):
    max_eaten_count = max(len(prey_list) for prey_list in data.values())
    most_flexible_eaters = [predator for predator, prey_list in data.items() if len(prey_list) == max_eaten_count]
    print("Most Flexible Eaters:", ", ".join(most_flexible_eaters))

def identify_tastiest_organisms(data):
    eaten_count = {}
    for prey_list in data.values():
        for prey in prey_list:
            eaten_count[prey] = eaten_count.get(prey, 0) + 1

    max_eaten = max(eaten_count.values())
    tastiest_organisms = [organism for organism, count in eaten_count.items() if count == max_eaten]
    print("Tastiest Organisms:", ", ".join(tastiest_organisms))

def determine_heights(data):
    heights = {predator: 0 for predator in data}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in data.items():
            for prey in prey_list:
                if heights[predator] <= heights.get(prey, -1):
                    heights[predator] = heights.get(prey, -1) + 1
                    changed = True

    for predator, height in sorted(heights.items()):
        print(predator + ":", height)

def main():
    if len(sys.argv) != 2:
        print("Usage: python food_web_analyzer.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        data = read_data(filename)
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)

    print("Predators and Prey:")
    list_predator_eats(data)
    print()

    identify_apex_predators(data)
    print()

    identify_producers(data)
    print()

    identify_most_flexible_eaters(data)
    print()

    identify_tastiest_organisms(data)
    print()

    print("Heights:")
    determine_heights(data)

if __name__ == "__main__":
    main()