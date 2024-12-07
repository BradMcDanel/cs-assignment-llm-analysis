# Your implementation of the Food Web analysis assignment goes here

import sys

def read_food_web_file(file_name):
    # Read the predator-prey relationships from the file and store them in a dictionary
    pass

def part1_predator_eats(data_dict):
    # List what each predator eats
    pass

def part2_apex_predators(data_dict):
    # Identify and display apex predators
    pass

def part3_producers(data_dict):
    # Identify and display producers
    pass

def part4_most_flexible_eaters(data_dict):
    # Identify and display the most flexible eaters
    pass

def part5_tastiest_organisms(data_dict):
    # Identify and display the tastiest organisms
    pass

def part6_height_of_organisms(data_dict):
    # Determine the height of each organism in the food web
    pass

def main():
    # Main function to orchestrate the analysis
    if len(sys.argv) < 2:
        file_name = input("Enter the name of the food web file: ")
    elif len(sys.argv) > 2:
        print("Error: Too many command line arguments. Please provide only the file name.")
        sys.exit(1)
    else:
        file_name = sys.argv[1]

    data_dict = read_food_web_file(file_name)

    part1_predator_eats(data_dict)
    part2_apex_predators(data_dict)
    part3_producers(data_dict)
    part4_most_flexible_eaters(data_dict)
    part5_tastiest_organisms(data_dict)
    part6_height_of_organisms(data_dict)

if __name__ == "__main__":
    main()

### formatList.py ###
## Format a list of items so that they are comma separated and "and" appears
#  before the last item.
#  Parameters:
#    data: the list of items to format
#  Returns: A string containing the items from data with nice formatting
def formatList(data):
    # Handle the case where the list is empty
    if len(data) == 0:
        return "(None)"
    
    # Start with an empty string that we will add items to
    retval = ""

    # Handle all of the items except for the last two
    for i in range(0, len(data) - 2):
        retval = retval + str(data[i]) + ", "

    # Handle the second last item
    if len(data) >= 2:
        retval += str(data[-2]) + " and "

    # Handle the last item
    retval += str(data[-1])

    # Return the result
    return retval