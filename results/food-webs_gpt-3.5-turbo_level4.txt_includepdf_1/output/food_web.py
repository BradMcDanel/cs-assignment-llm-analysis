import sys
import formatList

def read_file(file_name):
    data = {}
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip().split(',')
            data[line[0]] = line[1:]
    return data

def predators_and_prey(data):
    for predator, prey in data.items():
        prey_str = formatList.formatList(prey)
        print(f'{predator} eats {prey_str}')

def apex_predators(data):
    predators = set(data.keys())
    for prey_list in data.values():
        for prey in prey_list:
            if prey in predators:
                predators.remove(prey)
    print('Apex Predators:', formatList.formatList(list(predators)))

def producers(data):
    eaten = set()
    for prey_list in data.values():
        for prey in prey_list:
            eaten.add(prey)
    producers = set(data.keys()) - eaten
    print('Producers:', formatList.formatList(list(producers)))

# Implement other functions for parts 4 to 6

def main():
    if len(sys.argv) != 2:
        print('Usage: python food_web.py <file_name>')
        sys.exit(1)
    
    file_name = sys.argv[1]

    try:
        data = read_file(file_name)
    except FileNotFoundError:
        print('File not found.')
        sys.exit(1)

    print('Predators and Prey:')
    predators_and_prey(data)

    print()
    apex_predators(data)

    print()
    producers(data)

if __name__ == "__main__":
    main()