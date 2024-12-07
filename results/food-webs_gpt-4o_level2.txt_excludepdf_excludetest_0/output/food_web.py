import sys

def load_food_web(filename):
    try:
        with open(filename, 'r') as file:
            food_web = {}
            for line in file:
                parts = line.strip().split(',')
                predator = parts[0]
                prey = parts[1:]
                food_web[predator] = prey
        return food_web
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

def format_predator_prey(predator, prey_list):
    if len(prey_list) == 1:
        return f"{predator} eats {prey_list[0]}"
    else:
        return f"{predator} eats {', '.join(prey_list[:-1])} and {prey_list[-1]}"

def display_predator_prey(food_web):
    print("Predators and Prey:")
    for predator in sorted(food_web.keys()):
        print("  " + format_predator_prey(predator, sorted(food_web[predator])))

def main():
    if len(sys.argv) != 2:
        print("Usage: python food_web.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    food_web = load_food_web(filename)
    display_predator_prey(food_web)

if __name__ == "__main__":
    main()