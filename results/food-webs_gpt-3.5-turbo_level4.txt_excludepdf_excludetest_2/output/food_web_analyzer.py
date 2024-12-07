import sys

def read_food_web_file(filename):
    # Read the predator-prey relationships from the file and store them in a dictionary
    food_web_data = {}
    with open(filename, 'r') as file:
        for line in file:
            predator, *prey = line.strip().split(',')
            food_web_data[predator] = prey
    return food_web_data

def list_predator_prey_relationships(food_web_data):
    # List everything each predator eats
    for predator, prey_list in food_web_data.items():
        print(predator + " eats " + ', '.join(prey_list[:-1]) + " and " + prey_list[-1])

def identify_apex_predators(food_web_data):
    # Identify apex predators that are not eaten by any other organism
    apex_predators = [predator for predator in food_web_data if all(predator not in prey_list for prey_list in food_web_data.values())]
    print("Apex Predators: " + ', '.join(apex_predators))

# Implement functions for Part 3, 4, 5, and 6

def main():
    if len(sys.argv) != 2:
        print("Error: Please provide the food web file as a command line argument.")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        food_web_data = read_food_web_file(filename)
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

    print("Predators and Prey:")
    list_predator_prey_relationships(food_web_data)
    
    identify_apex_predators(food_web_data)

    # Call functions for Part 3, 4, 5, and 6

if __name__ == "__main__":
    main()