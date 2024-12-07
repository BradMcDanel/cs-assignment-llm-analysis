# Print the name of the subject of the fatal police shooting with ID number 1694
subject_1694_name = database[1694]["name"]
print(subject_1694_name)

# Print the name of all subjects of fatal police shootings in Minnesota
for entry_id, details in database.items():
    if details["state"] == "MN":
        print(details["name"])

# Create a new dictionary to count the number of occurrences of each race
race_counts = {}
for entry_id, details in database.items():
    race = details["race"]
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Calculate and print the fraction of fatal police shootings with a black subject
black_shootings = race_counts.get('B', 0)
total_shootings = len(database)
black_fraction = black_shootings / total_shootings
print(black_fraction)

# Create a new dictionary for unarmed fatal police shootings
unarmed_selection = {}
for entry_id, details in database.items():
    if details["armed"] == "unarmed":
        unarmed_selection[entry_id] = details

# Create a new dictionary to count the number of occurrences of each race among unarmed subjects
unarmed_race_counts = {}
for entry_id, details in unarmed_selection.items():
    race = details["race"]
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Calculate and print the fraction of unarmed fatal police shootings with a black subject
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
total_unarmed_shootings = len(unarmed_selection)
unarmed_black_fraction = unarmed_black_shootings / total_unarmed_shootings
print(unarmed_black_fraction)