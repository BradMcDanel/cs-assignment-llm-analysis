import sys
from food_web import (
    load_food_web,
    display_predators_and_prey,
    identify_apex_predators,
    identify_producers,
    identify_most_flexible_eaters,
    identify_tastiest_organisms,
    determine_organism_heights
)

def main():
    if len(sys.argv) < 2:
        filename = input("Enter the name of the food web file: ")
    elif len(sys.argv) > 2:
        print("Error: Too many command line arguments provided.")
        return
    else:
        filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            food_web = load_food_web(file)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return

    print("Predators and Prey:")
    display_predators_and_prey(food_web)

    print("\nApex Predators:", identify_apex_predators(food_web))
    print("\nProducers:", identify_producers(food_web))
    print("\nMost Flexible Eaters:", identify_most_flexible_eaters(food_web))
    print("\nTastiest:", identify_tastiest_organisms(food_web))

    print("\nHeights:")
    heights = determine_organism_heights(food_web)
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

if __name__ == "__main__":
    main()