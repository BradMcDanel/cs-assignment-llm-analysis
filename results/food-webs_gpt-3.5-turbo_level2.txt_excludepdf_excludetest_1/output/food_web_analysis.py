import sys
import csv
from formatting import format_output

def read_food_web_file(file_name):
    predator_prey_dict = {}
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            predator = line[0]
            prey = line[1:]
            predator_prey_dict[predator] = prey
    return predator_prey_dict

def part1(predator_prey_dict):
    print("Predators and Prey:")
    for predator, prey_list in sorted(predator_prey_dict.items()):
        formatted_output = format_output(predator, prey_list)
        print(formatted_output)

def part2(predator_prey_dict):
    apex_predators = []
    for predator in predator_prey_dict.keys():
        eaten_by_other = False
        for prey_list in predator_prey_dict.values():
            if predator in prey_list:
                eaten_by_other = True
                break
        if not eaten_by_other:
            apex_predators.append(predator)
    print("Apex Predators:", ', '.join(apex_predators))

# Define other parts (3 to 6) functions here

def main():
    if len(sys.argv) < 2:
        file_name = input("Enter the name of the food web file: ")
    elif len(sys.argv) > 2:
        print("Error: Too many command line arguments provided.")
        sys.exit()

    file_name = sys.argv[1]

    try:
        predator_prey_dict = read_food_web_file(file_name)
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit()

    part1(predator_prey_dict)
    part2(predator_prey_dict)
    # Call other parts functions here

if __name__ == "__main__":
    main()