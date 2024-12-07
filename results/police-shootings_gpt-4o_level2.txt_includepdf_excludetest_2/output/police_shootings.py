# Existing code...

# Print the name of the subject of the fatal police shooting with ID number 1694
print("Name of subject with ID 1694:", database[1694]["name"])

# Print the names of all subjects of fatal police shootings in Minnesota
print("Fatal police shootings in Minnesota:")
for entry_id, entry in database.items():
    if entry["state"] == "MN":
        print(entry["name"])

# Create a dictionary to count occurrences of each race
race_counts = {}
for entry in database.values():
    race = entry["race"]
    if race not in race_counts:
        race_counts[race] = 0
    race_counts[race] += 1

# Calculate and print the fraction of fatal police shootings with a black subject
black_shootings = race_counts.get("B", 0)
total_shootings = len(database)
black_fraction = black_shootings / total_shootings
print("Fraction of fatal police shootings with a black subject:", black_fraction)

# Create a dictionary for unarmed fatal police shootings
unarmed_selection = {entry_id: entry for entry_id, entry in database.items() if entry["armed"] == "unarmed"}

# Create a dictionary to count occurrences of each race for unarmed subjects
unarmed_race_counts = {}
for entry in unarmed_selection.values():
    race = entry["race"]
    if race not in unarmed_race_counts:
        unarmed_race_counts[race] = 0
    unarmed_race_counts[race] += 1

# Calculate and print the fraction of unarmed fatal police shootings with a black subject
unarmed_black_shootings = unarmed_race_counts.get("B", 0)
total_unarmed_shootings = len(unarmed_selection)
unarmed_black_fraction = unarmed_black_shootings / total_unarmed_shootings
print("Fraction of unarmed fatal police shootings with a black subject:", unarmed_black_fraction)