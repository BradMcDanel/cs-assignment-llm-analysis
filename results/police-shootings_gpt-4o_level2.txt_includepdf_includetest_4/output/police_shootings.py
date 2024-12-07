# Assuming previous code is already in place...

# Print the name of the subject with ID 1694
print("Name of subject with ID 1694:", database[1694]["name"])

# Print names of all subjects of fatal police shootings in Minnesota
print("Subjects of fatal police shootings in Minnesota:")
for entry_id, details in database.items():
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

# Calculate the fraction of fatal police shootings with a black subject
black_count = race_counts.get("B", 0)
total_shootings = len(database)
black_fraction = black_count / total_shootings
print("Fraction of fatal police shootings with a black subject:", black_fraction)

# Create a dictionary for unarmed shootings
unarmed_selection = {entry_id: details for entry_id, details in database.items() if details["armed"] == "unarmed"}

# Create a dictionary to count occurrences of each race in unarmed shootings
unarmed_race_counts = {}
for details in unarmed_selection.values():
    race = details["race"]
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Calculate the fraction of unarmed fatal police shootings with a black subject
unarmed_black_count = unarmed_race_counts.get("B", 0)
total_unarmed_shootings = len(unarmed_selection)
unarmed_black_fraction = unarmed_black_count / total_unarmed_shootings
print("Fraction of unarmed fatal police shootings with a black subject:", unarmed_black_fraction)