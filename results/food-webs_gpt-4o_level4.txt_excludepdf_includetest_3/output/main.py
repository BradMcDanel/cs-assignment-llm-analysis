import sys
from food_web import process_food_web, find_apex_predators, find_producers, find_most_flexible_eaters, find_tastiest_organisms, determine_heights

def main():
    # Handle command line arguments
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    elif len(sys.argv) < 2:
        file_name = input("Enter the name of the food web file: ")
    else:
        print("Error: Too many command line arguments provided.")
        sys.exit(1)
    
    # Attempt to open the file
    try:
        with open(file_name, 'r') as file:
            food_web = process_food_web(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        sys.exit(1)
    
    # Part 1: Display predators and their prey
    print("Predators and Prey:")
    for predator, prey in sorted(food_web.items()):
        print(f"  {predator} eats {', '.join(prey[:-1])} and {prey[-1]}")
    
    # Part 2: Identify the apex predators
    apex_predators = find_apex_predators(food_web)
    print(f"\nApex Predators: {', '.join(apex_predators)}")
    
    # Part 3: Identify the producers
    producers = find_producers(food_web)
    print(f"\nProducers: {', '.join(producers)}")
    
    # Part 4: Identify the most flexible eaters
    most_flexible_eaters = find_most_flexible_eaters(food_web)
    print(f"\nMost Flexible Eaters: {', '.join(most_flexible_eaters)}")
    
    # Part 5: Identify the tastiest organisms
    tastiest_organisms = find_tastiest_organisms(food_web)
    print(f"\nTastiest: {', '.join(tastiest_organisms)}")
    
    # Part 6: Determine the height of each organism
    heights = determine_heights(food_web)
    print("\nHeights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

if __name__ == "__main__":
    main()