# Task 3: Using the database

# Print the name of the subject of the fatal police shooting with ID number 1694
print(database[1694]["name"])

# Print the name of all subjects of fatal police shootings in Minnesota in the dataset
for key, value in database.items():
    if value["state"] == "MN":
        print(value["name"])

# Create a new dictionary, race counts, to count the number of occurrences of each race among subjects
race_counts = {}
for key, value in database.items():
    race = value["race"]
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Print the fraction of fatal police shootings with a black subject
total_shootings = len(database)
black_shootings = race_counts.get("B", 0)
fraction_black_shootings = black_shootings / total_shootings
print(fraction_black_shootings)