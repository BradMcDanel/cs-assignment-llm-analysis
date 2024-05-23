import sys
from food_web import load_food_web, list_predators_and_prey, find_apex_predators, find_producers, find_most_flexible_eaters, find_tastiest_organisms, calculate_heights

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    elif len(sys.argv) == 1:
        filename = input("Please enter the filename: ")
    else:
        print("Error: Too many command line arguments.")
        return

    try:
        food_web = load_food_web(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    print("Predators and Prey:")
    list_predators_and_prey(food_web)

    apex_predators = find_apex_predators(food_web)
    print(f"\nApex Predators: {', '.join(apex_predators)}")

    producers = find_producers(food_web)
    print(f"\nProducers: {', '.join(producers)}")

    most_flexible_eaters = find_most_flexible_eaters(food_web)
    print(f"\nMost Flexible Eaters: {', '.join(most_flexible_eaters)}")

    tastiest_organisms = find_tastiest_organisms(food_web)
    print(f"\nTastiest: {', '.join(tastiest_organisms)}")

    heights = calculate_heights(food_web)
    print("\nHeights:")
    for organism, height in heights.items():
        print(f"  {organism}: {height}")

if __name__ == "__main__":
    main()