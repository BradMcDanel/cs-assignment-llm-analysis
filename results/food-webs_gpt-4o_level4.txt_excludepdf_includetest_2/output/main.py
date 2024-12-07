import sys
from formatter import format_predator_and_prey
from food_web import (load_food_web, get_apex_predators, get_producers, 
                      get_most_flexible_eaters, get_tastiest_organisms, calculate_heights)

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <filename>")
        return
    
    filename = sys.argv[1]
    food_web = load_food_web(filename)
    
    print("Predators and Prey:")
    for predator, prey_list in sorted(food_web.items()):
        print("  " + format_predator_and_prey(predator, prey_list))
    
    apex_predators = get_apex_predators(food_web)
    print("\nApex Predators: " + ", ".join(sorted(apex_predators)))
    
    producers = get_producers(food_web)
    print("\nProducers: " + " and ".join(sorted(producers)))
    
    flexible_eaters = get_most_flexible_eaters(food_web)
    print("\nMost Flexible Eaters: " + ", ".join(sorted(flexible_eaters)))
    
    tastiest_organisms = get_tastiest_organisms(food_web)
    print("\nTastiest: " + " and ".join(sorted(tastiest_organisms)))
    
    heights = calculate_heights(food_web)
    print("\nHeights:")
    for animal, height in sorted(heights.items()):
        print(f"  {animal}: {height}")

if __name__ == "__main__":
    main()