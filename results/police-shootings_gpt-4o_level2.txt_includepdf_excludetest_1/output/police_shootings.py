# Continue after the provided code

# Print the name of the subject with ID 1694
subject_1694 = database.get(1694, {}).get("name", "Name not found")
print(f"Name of subject with ID 1694: {subject_1694}")

# Print the names of all subjects of fatal police shootings in Minnesota
print("Subjects of fatal police shootings in Minnesota:")
for entry_id, details in database.items():
    if details["state"] == "MN":
        print(details["name"])

# Create a new dictionary to count occurrences of each race
race_counts = {}
for entry_id, details in database.items():
    race = details["race"]
    if race not in race_counts:
        race_counts[race] = 0
    race_counts[race] += 1

# Calculate the fraction of fatal police shootings with a black subject
black_shootings = race_counts.get('B', 0)
total_shootings = len(database)
black_shooting_fraction = black_shootings / total_shootings
print(f"Fraction of fatal police shootings with a black subject: {black_shooting_fraction:.4f}")

# Create a dictionary for unarmed shootings
unarmed_selection = {}
for entry_id, details in database.items():
    if details["armed"] == "unarmed":
        unarmed_selection[entry_id] = details

# Create a race count dictionary for unarmed shootings
unarmed_race_counts = {}
for entry_id, details in unarmed_selection.items():
    race = details["race"]
    if race not in unarmed_race_counts:
        unarmed_race_counts[race] = 0
    unarmed_race_counts[race] += 1

# Calculate the fraction of unarmed fatal police shootings with a black subject
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
total_unarmed_shootings = len(unarmed_selection)
unarmed_black_shooting_fraction = unarmed_black_shootings / total_unarmed_shootings
print(f"Fraction of unarmed fatal police shootings with a black subject: {unarmed_black_shooting_fraction:.4f}")