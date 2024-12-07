import sys

def read_food_web(file_name):
    # Read the food web file and store the relationships in a dictionary
    food_web_dict = {}
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            predator = parts[0]
            prey = parts[1:]
            food_web_dict[predator] = prey
    return food_web_dict

def list_predators_and_prey(food_web_dict):
    # List everything each predator eats with nice formatting
    for predator, prey in food_web_dict.items():
        print(f"{predator} eats {formatList(prey)}")

def identify_apex_predators(food_web_dict):
    # Identify and display all apex predators
    apex_predators = [predator for predator in food_web_dict.keys() if predator not in set(sum(food_web_dict.values(), []))]
    print("Apex Predators:", formatList(apex_predators))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        file_name = input("Enter the food web file name: ")
    elif len(sys.argv) > 2:
        print("Error: Too many command line arguments provided.")
        sys.exit()
    else:
        file_name = sys.argv[1]

    try:
        food_web_dict = read_food_web(file_name)
        list_predators_and_prey(food_web_dict)
        identify_apex_predators(food_web_dict)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred:", e)