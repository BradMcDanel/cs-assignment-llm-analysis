# Import necessary libraries
import csv

# Open the CSV file and read data into a dictionary
with open("fatal-police-shootings-data.csv", mode='r') as file:
    # Use csv.DictReader to automatically read and map header row to dictionary keys
    reader = csv.DictReader(file)
    database = {}
    for row in reader:
        # Create a dictionary entry where the key is the 'id' and the value is a dictionary of selected attributes
        database[int(row["id"])] = {
            "name": row["name"],
            "date": row["date"],
            "state": row["state"],
            "race": row["race"],
            "armed": row["armed_with"],
            "age": row["age"],
            "gender": row["gender"]
        }

# Task 3: Additional code for analysis
# Print the name of the subject with ID number 1694
print("Name of the subject with ID 1694:", database[1694]["name"])

# Print names of all subjects from Minnesota
print("Subjects from Minnesota:")
for id, details in database.items():
    if details["state"] == "MN":
        print(details["name"])

# Create a dictionary to count occurrences of each race
race_counts = {}
for details in database.values():
    race = details["race"]
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Print the fraction of fatal police shootings with a black subject
total_shootings = len(database)
black_shootings = race_counts.get("B", 0)
print("Fraction of fatal police shootings with a black subject:", black_shootings / total_shootings)

# Creating a dictionary for unarmed shootings
unarmed_selection = {id: val for id, val in database.items() if val["armed"] == "unarmed"}

# Count occurrences of each race among unarmed subjects
unarmed_race_counts = {}
for details in unarmed_selection.values():
    race = details["race"]
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Print the fraction of unarmed shootings with a black subject
total_unarmed_shootings = len(unarmed_selection)
black_unarmed_shootings = unarmed_race_counts.get("B", 0)
print("Fraction of unarmed fatal shootings with a black subject:", black_unarmed_shootings / total_unarmed_shootings)