# Print the name of the subject of the fatal police shooting with ID number 1694
print("Name of the subject with ID 1694:", database[1694]["name"])

# Print the name of all subjects of fatal police shootings in Minnesota
print("Names of subjects of fatal police shootings in Minnesota:")
for entry_id, details in database.items():
    if details["state"] == "MN":
        print(details["name"])

# Create a new dictionary to count the number of occurrences of each race
race_counts = {}
for entry_id, details in database.items():
    race = details["race"]
    if race not in race_counts:
        race_counts[race] = 0
    race_counts[race] += 1

# Calculate and print the fraction of fatal police shootings with a black subject
black_shootings = race_counts.get('B', 0)
total_shootings = len(database)
fraction_black = black_shootings / total_shootings
print("Fraction of fatal police shootings with a black subject:", fraction_black)

# Create a new dictionary for unarmed subjects
unarmed_selection = {}
for entry_id, details in database.items():
    if details["armed"] == "unarmed":
        unarmed_selection[entry_id] = details

# Create a new dictionary to count the number of occurrences of each race among unarmed subjects
unarmed_race_counts = {}
for entry_id, details in unarmed_selection.items():
    race = details["race"]
    if race not in unarmed_race_counts:
        unarmed_race_counts[race] = 0
    unarmed_race_counts[race] += 1

# Calculate and print the fraction of unarmed fatal police shootings with a black subject
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
total_unarmed_shootings = len(unarmed_selection)
fraction_unarmed_black = unarmed_black_shootings / total_unarmed_shootings
print("Fraction of unarmed fatal police shootings with a black subject:", fraction_unarmed_black)