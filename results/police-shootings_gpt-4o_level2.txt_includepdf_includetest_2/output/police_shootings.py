# Existing code for reading data

# Print the name of the subject with ID 1694
print(database[1694]["name"])

# Print names of all subjects in Minnesota
for entry_id, entry_data in database.items():
    if entry_data["state"] == "MN":
        print(entry_data["name"])

# Create a dictionary to count occurrences of each race
race_counts = {}
for entry_data in database.values():
    race = entry_data["race"]
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Calculate and print the fraction of shootings with a black subject
black_fraction = race_counts.get("B", 0) / len(database)
print(black_fraction)

# Create a dictionary for unarmed shootings
unarmed_selection = {}
for entry_id, entry_data in database.items():
    if entry_data["armed"].lower() == "unarmed":
        unarmed_selection[entry_id] = entry_data

# Count occurrences of each race in unarmed shootings
unarmed_race_counts = {}
for entry_data in unarmed_selection.values():
    race = entry_data["race"]
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Calculate and print the fraction of unarmed shootings with a black subject
unarmed_black_fraction = unarmed_race_counts.get("B", 0) / len(unarmed_selection)
print(unarmed_black_fraction)