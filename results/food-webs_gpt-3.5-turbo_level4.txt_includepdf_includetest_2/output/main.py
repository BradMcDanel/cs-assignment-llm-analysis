import sys
from formatList import formatList

def read_food_web(file_name):
    # Read the food web file and return the contents
    pass

def part1(predator_prey_dict):
    # Implement Part 1: What do the Predators Eat?
    pass

def part2(predator_prey_dict):
    # Implement Part 2: Identify the Apex Predators
    pass

def part3(predator_prey_dict):
    # Implement Part 3: Identify the Producers
    pass

def part4(predator_prey_dict):
    # Implement Part 4: Identify the Most Flexible Eaters
    pass

def part5(predator_prey_dict):
    # Implement Part 5: The Tastiest Organism
    pass

def part6(predator_prey_dict):
    # Implement Part 6: Determine the Height of Each Organism in the Food Web
    pass

def main():
    if len(sys.argv) == 1:
        file_name = input("Enter the name of the food web file: ")
    elif len(sys.argv) == 2:
        file_name = sys.argv[1]
    else:
        print("Error: Please provide only one command line argument.")
        return

    # Read the food web file
    predator_prey_dict = read_food_web(file_name)

    if not predator_prey_dict:
        return

    part1(predator_prey_dict)
    part2(predator_prey_dict)
    part3(predator_prey_dict)
    part4(predator_prey_dict)
    part5(predator_prey_dict)
    part6(predator_prey_dict)

if __name__ == "__main__":
    main()