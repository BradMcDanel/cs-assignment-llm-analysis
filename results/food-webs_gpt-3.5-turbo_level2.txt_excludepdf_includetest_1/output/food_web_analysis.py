import sys
from formatting import format_output

def load_data(file_name):
    data = {}
    with open(file_name) as file:
        for line in file:
            line = line.strip().split(',')
            predator = line[0]
            prey = line[1:]
            data[predator] = prey
    return data

def list_predator_prey(data):
    for predator, prey_list in data.items():
        formatted_prey = format_output(prey_list)
        print(f'{predator} eats {formatted_prey}')

def identify_apex_predators(data):
    apex_predators = [predator for predator in data if all(predator not in values for values in data.values())]
    print('Apex Predators:', ', '.join(apex_predators))

def identify_producers(data):
    producers = [predator for predator, prey_list in data.items() if not prey_list]
    print('Producers:', ', '.join(producers))

def identify_most_flexible_eaters(data):
    max_eaten_count = max(len(prey_list) for prey_list in data.values())
    most_flexible_eaters = [predator for predator, prey_list in data.items() if len(prey_list) == max_eaten_count]
    print('Most Flexible Eaters:', ', '.join(most_flexible_eaters))

def identify_tastiest_organisms(data):
    eaten_by_count = {prey: sum(prey in values for values in data.values()) for prey in set(p for values in data.values() for p in values)}
    max_eaten_count = max(eaten_by_count.values())
    tastiest_organisms = [organism for organism, count in eaten_by_count.items() if count == max_eaten_count]
    print('Tastiest Organisms:', ', '.join(tastiest_organisms))

def determine_heights(data):
    heights = {organism: 0 for organism in data}
    changed = True
    while changed:
        changed = False
        for predator, prey_list in data.items():
            for prey in prey_list:
                if heights[predator] <= heights.get(prey, -1):
                    heights[predator] = heights.get(prey, -1) + 1
                    changed = True
    print('Heights:')
    for organism, height in heights.items():
        print(f'  {organism}: {height}')

def main():
    file_name = sys.argv[1] if len(sys.argv) > 1 else input('Enter the name of the file: ')
    try:
        data = load_data(file_name)
        print('Predators and Prey:')
        list_predator_prey(data)
        identify_apex_predators(data)
        identify_producers(data)
        identify_most_flexible_eaters(data)
        identify_tastiest_organisms(data)
        determine_heights(data)
    except FileNotFoundError:
        print('File not found.')

if __name__ == '__main__':
    main()