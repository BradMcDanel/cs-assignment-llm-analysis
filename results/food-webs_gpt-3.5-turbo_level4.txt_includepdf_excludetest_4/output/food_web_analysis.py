import sys

## Function to format the list of items as specified in the assignment
def format_list(data):
    if len(data) == 0:
        return "(None)"
    
    retval = ""
    
    for i in range(0, len(data) - 2):
        retval = retval + str(data[i]) + ", "
    
    if len(data) >= 2:
        retval += str(data[-2]) + " and "
    
    retval += str(data[-1])
    
    return retval

## Function to read the predator-prey relationships from a file and store them in a dictionary
def read_food_web(file_name):
    food_web = {}
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            predator = parts[0]
            prey = parts[1:]
            food_web[predator] = prey
    
    return food_web

## Function to list everything each predator eats
def list_predator_eats(food_web):
    for predator, prey in food_web.items():
        formatted_prey = format_list(prey)
        print(f"{predator} eats {formatted_prey}")

## Function to identify the apex predators
def identify_apex_predators(food_web):
    apex_predators = []
    for predator in food_web.keys():
        is_apex = True
        for prey_list in food_web.values():
            if predator in prey_list:
                is_apex = False
                break
        if is_apex:
            apex_predators.append(predator)
    
    print("Apex Predators:", format_list(apex_predators))

## Function to identify the producers
def identify_producers(food_web):
    producers = []
    for predator, prey in food_web.items():
        if not prey:
            producers.append(predator)
    
    print("Producers:", format_list(producers))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    else:
        file_name = input("Enter the name of the file: ")
    
    try:
        food_web_data = read_food_web(file_name)
        print("Predators and Prey:")
        list_predator_eats(food_web_data)
        
        identify_apex_predators(food_web_data)
        
        identify_producers(food_web_data)
    except FileNotFoundError:
        print("Error: File not found.")