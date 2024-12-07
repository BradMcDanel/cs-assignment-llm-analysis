def calculate_heights(relationships):
    heights = {predator: 0 for predator in relationships}
    changed = True

    while changed:
        changed = False
        for predator, prey in relationships.items():
            for animal in prey:
                if heights[animal] >= heights[predator]:
                    heights[predator] = heights[animal] + 1
                    changed = True

    return heights

def part_6(data):
    relationships = process_data(data)
    heights = calculate_heights(relationships)
    for animal, height in sorted(heights.items()):
        print(f"{animal}: {height}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments.")
        sys.exit()
    
    file_name = sys.argv[1]
    file_data = read_file(file_name)
    part_6(file_data)