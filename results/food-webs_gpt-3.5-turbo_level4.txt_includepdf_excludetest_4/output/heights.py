import sys

## Function to determine the height of each organism in the food web
def determine_heights(food_web):
    heights = {organism: 0 for organism in food_web.keys()}
    changed = True
    
    while changed:
        changed = False
        for animal, prey in food_web.items():
            for p in prey:
                if heights[animal] <= heights[p]:
                    heights[animal] = heights[p] + 1
                    changed = True
    
    for animal, height in heights.items():
        print(f"{animal}: {height}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    else:
        file_name = input("Enter the name of the file: ")
    
    try:
        food_web_data = read_food_web(file_name)
        print("Heights:")
        determine_heights(food_web_data)
    except FileNotFoundError:
        print("Error: File not found.")