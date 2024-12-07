import sys
from formatoutput import format_output

def load_data(filename):
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().split(',')
            predator = line[0]
            prey = line[1:]
            data[predator] = prey
    return data

def list_predators_and_prey(data):
    for predator, prey in data.items():
        output = f"{predator} eats "
        if len(prey) > 1:
            output += ", ".join(prey[:-1]) + " and " + prey[-1]
        else:
            output += prey[0]
        print(format_output(output))

def identify_apex_predators(data):
    apex_predators = []
    for predator in data.keys():
        eaten_by_other = False
        for value in data.values():
            if predator in value:
                eaten_by_other = True
                break
        if not eaten_by_other:
            apex_predators.append(predator)
    print("Apex Predators:", ", ".join(apex_predators))

def identify_producers(data):
    producers = []
    for predator in data.keys():
        eaten = False
        for value in data.values():
            if predator in value:
                eaten = True
                break
        if not eaten:
            producers.append(predator)
    print("Producers:", ", ".join(producers))

def identify_most_flexible_eaters(data):
    max_eats = max([len(value) for value in data.values()])
    flexible_eaters = [key for key, value in data.items() if len(value) == max_eats]
    print("Most Flexible Eaters:", ", ".join(flexible_eaters))

def identify_tastiest_organisms(data):
    all_prey = [prey for value in data.values() for prey in value]
    prey_count = {prey: all_prey.count(prey) for prey in set(all_prey)}
    max_count = max(prey_count.values())
    tastiest_organisms = [prey for prey, count in prey_count.items() if count == max_count]
    print("Tastiest Organisms:", ", ".join(tastiest_organisms))

def determine_heights(data):
    heights = {predator: 0 for predator in data.keys()}
    changed = True
    while changed:
        changed = False
        for predator, prey in data.items():
            for p in prey:
                if heights[predator] <= heights.get(p, -1):
                    heights[predator] = heights[p] + 1
                    changed = True
    for predator, height in heights.items():
        print(predator + ":", height)

def main():
    if len(sys.argv) != 2:
        print("Error: Incorrect number of arguments")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        data = load_data(filename)
    except FileNotFoundError:
        print("Error: File not found")
        sys.exit(1)

    list_predators_and_prey(data)
    identify_apex_predators(data)
    identify_producers(data)
    identify_most_flexible_eaters(data)
    identify_tastiest_organisms(data)
    determine_heights(data)

if __name__ == "__main__":
    main()