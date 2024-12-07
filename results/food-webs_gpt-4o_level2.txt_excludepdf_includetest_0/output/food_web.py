def determine_heights(food_web):
    heights = {organism: 0 for organism in food_web}
    changed = True
    while changed:
        changed = False
        for predator, preys in food_web.items():
            for prey in preys:
                if heights[predator] <= heights[prey]:
                    heights[predator] = heights[prey] + 1
                    changed = True
    return heights

def display_heights(food_web):
    heights = determine_heights(food_web)
    print("Heights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

def main():
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    elif len(sys.argv) == 1:
        file_name = input("Enter the name of the file: ")
    else:
        print("Error: Too many command line arguments provided.")
        sys.exit(1)

    data = read_file(file_name)
    food_web = parse_data(data)
    display_predators_and_prey(food_web)
    display_apex_predators(food_web)
    display_producers(food_web)
    display_most_flexible_eaters(food_web)
    display_tastiest_organisms(food_web)
    display_heights(food_web)

if __name__ == "__main__":
    main()