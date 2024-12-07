import sys
from formatList import formatList

# Function to read the data file and load the predator-prey relationships into a dictionary
def read_data(filename):
    data_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            predator = parts[0]
            prey = parts[1:]
            data_dict[predator] = prey
    return data_dict

# Part 1: What do the Predators Eat?
def part1(data_dict):
    print("Predators and Prey:")
    for predator, prey in sorted(data_dict.items()):
        formatted_prey = formatList(prey)
        print(f"  {predator} eats {formatted_prey}")

# Part 2: Identify the Apex Predators
def part2(data_dict):
    print("Apex Predators:", ", ".join([predator for predator in data_dict if all(predator not in prey_list for prey_list in data_dict.values())]))

# Part 3: Identify the Producers
def part3(data_dict):
    print("Producers:", ", ".join([predator for predator, prey in data_dict.items() if not prey]))

# Part 4: Identify the Most Flexible Eaters
def part4(data_dict):
    max_eaten = max(len(prey) for prey in data_dict.values())
    print("Most Flexible Eaters:", ", ".join([predator for predator, prey in data_dict.items() if len(prey) == max_eaten]))

# Part 5: Identify the Tastiest Organism
def part5(data_dict):
    prey_counts = {}
    for prey_list in data_dict.values():
        for prey in prey_list:
            prey_counts[prey] = prey_counts.get(prey, 0) + 1
    max_count = max(prey_counts.values())
    print("Tastiest:", ", ".join([prey for prey, count in prey_counts.items() if count == max_count]))

# Part 6: Determine the Height of Each Organism in the Food Web
def part6(data_dict):
    heights = {predator: 0 for predator in data_dict}
    changed = True
    while changed:
        changed = False
        for predator, prey in data_dict.items():
            for p in prey:
                if heights[predator] <= heights.get(p, -1):
                    heights[predator] = heights[p] + 1
                    changed = True
    print("Heights:")
    for predator, height in sorted(heights.items()):
        print(f"  {predator}: {height}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Assignment4.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        data_dict = read_data(filename)
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)

    part1(data_dict)
    part2(data_dict)
    part3(data_dict)
    part4(data_dict)
    part5(data_dict)
    part6(data_dict)