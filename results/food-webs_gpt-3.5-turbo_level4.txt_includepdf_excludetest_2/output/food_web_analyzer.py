import sys

def read_food_web_file(filename):
    # Read the file and store the predator-prey relationships in a dictionary
    # Keys are predators, and values are lists of prey
    food_web = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().split(',')
            predator = line[0]
            prey = line[1:]
            food_web[predator] = prey
    return food_web

def what_predators_eat(food_web):
    # Part 1: List everything each predator eats on a single line with nice formatting
    for predator, prey in food_web.items():
        print(predator + " eats " + formatList(prey))

def identify_apex_predators(food_web):
    # Part 2: Identify and display all apex predators
    apex_predators = [predator for predator in food_web.keys() if predator not in set(sum(food_web.values(), []))]
    print("Apex Predators:", formatList(apex_predators))

# Implement the other parts (3 to 6) following similar function structure

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Please provide the food web file as a command line argument.")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    try:
        food_web_data = read_food_web_file(filename)
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    
    # Call each part's function
    what_predators_eat(food_web_data)
    identify_apex_predators(food_web_data)