def main():
    if len(sys.argv) < 2:
        filename = input("Enter the name of the food web file: ")
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print("Error: Too many command line arguments provided.")
        sys.exit(1)
    
    predator_prey_data = load_predator_prey_relationships(filename)
    
    display_predators_and_prey(predator_prey_data)
    display_apex_predators(predator_prey_data)
    display_producers(predator_prey_data)
    display_most_flexible_eaters(predator_prey_data)
    display_tastiest_organisms(predator_prey_data)
    display_heights(predator_prey_data)

if __name__ == "__main__":
    main()