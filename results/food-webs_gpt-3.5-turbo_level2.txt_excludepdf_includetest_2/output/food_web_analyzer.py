import sys
import formatting_module

def read_food_web_data(filename):
    # Read the predator-prey relationships from the file and store in a dictionary
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().split(',')
            predator = line[0]
            prey = line[1:]
            data[predator] = prey
    return data

def part1(data):
    print("Predators and Prey:")
    for predator, prey_list in sorted(data.items()):
        formatted_prey = formatting_module.format_prey_list(prey_list)
        print(f"  {predator} eats {formatted_prey}")

def part2(data):
    apex_predators = [predator for predator in data if not any(predator in prey for prey in data.values())]
    print("\nApex Predators:", ', '.join(apex_predators))

def part3(data):
    producers = [predator for predator, prey in data.items() if not prey]
    print("\nProducers:", ', '.join(producers))

def part4(data):
    max_eater_count = max(len(prey) for prey in data.values())
    most_flexible_eaters = [predator for predator, prey in data.items() if len(prey) == max_eater_count]
    print("\nMost Flexible Eaters:", ', '.join(most_flexible_eaters))

def part5(data):
    prey_counts = {}
    for prey_list in data.values():
        for prey in prey_list:
            prey_counts[prey] = prey_counts.get(prey, 0) + 1
    tastiest_organisms = [organism for organism, count in prey_counts.items() if count == max(prey_counts.values())]
    print("\nTastiest Organisms:", ', '.join(tastiest_organisms))

def part6(data):
    heights = {}
    for predator in data:
        height = 0
        current_predator = predator
        while current_predator in data:
            height += 1
            current_predator = next((key for key, value in data.items() if current_predator in value), None)
        heights[predator] = height
    print("\nHeights:")
    for organism, height in sorted(heights.items()):
        print(f"  {organism}: {height}")

def main():
    if len(sys.argv) != 2:
        print("Error: Please provide the food web file name as a command line argument.")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        food_web_data = read_food_web_data(filename)
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    
    part1(food_web_data)
    part2(food_web_data)
    part3(food_web_data)
    part4(food_web_data)
    part5(food_web_data)
    part6(food_web_data)

if __name__ == "__main__":
    main()