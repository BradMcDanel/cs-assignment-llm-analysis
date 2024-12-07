# Add this function after the previous ones
def determine_heights(food_web):
    heights = {organism: 0 for organism in food_web}
    changed = True

    while changed:
        changed = False
        for predator, prey_list in food_web.items():
            for prey in prey_list:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True

    return heights

# Modify the main function to include this part
def main():
    if len(sys.argv) > 2:
        print("Error: Too many command line arguments.")
        sys.exit(1)
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input("Enter the name of the food web file: ")

    food_web = load_food_web(filename)
    formatted_lines = format_predator_prey(food_web)
    for line in formatted_lines:
        print(line)
    
    apex_predators = find_apex_predators(food_web)
    print("\nApex Predators: " + ', '.join(apex_predators))

    producers = find_producers(food_web)
    print("\nProducers: " + ', '.join(producers))

    most_flexible_eaters = find_most_flexible_eaters(food_web)
    print("\nMost Flexible Eaters: " + ', '.join(most_flexible_eaters))

    tastiest_organisms = find_tastiest_organisms(food_web)
    print("\nTastiest: " + ', '.join(tastiest_organisms))

    heights = determine_heights(food_web)
    print("\nHeights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

if __name__ == "__main__":
    main()