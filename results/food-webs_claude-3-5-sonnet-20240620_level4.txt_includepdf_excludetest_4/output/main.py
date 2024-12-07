import sys
from food_web_analyzer import analyze_food_web

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    elif len(sys.argv) == 1:
        filename = input("Enter the name of the food web file: ")
    else:
        print("Error: Invalid number of command line arguments.")
        sys.exit(1)

    analyze_food_web(filename)

if __name__ == "__main__":
    main()