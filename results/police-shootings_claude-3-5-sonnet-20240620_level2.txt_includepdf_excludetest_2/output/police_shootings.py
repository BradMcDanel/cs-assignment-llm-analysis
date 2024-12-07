# ... (previous code remains the same)

# Print the name of the subject with ID number 1694
print(f"Subject with ID 1694: {database[1694]['name']}")

# Print names of all subjects in Minnesota
print("Subjects in Minnesota:")
for id, entry in database.items():
    if entry['state'] == 'MN':
        print(entry['name'])

# Create race_counts dictionary
race_counts = {}
for entry in database.values():
    race = entry['race']
    race_counts[race] = race_counts.get(race, 0) + 1

# Calculate and print the fraction of shootings with a black subject
total_shootings = len(database)
black_shootings = race_counts.get('B', 0)
black_fraction = black_shootings / total_shootings
print(f"Fraction of shootings with a black subject: {black_fraction:.4f}")

# Create unarmed_selection dictionary
unarmed_selection = {}
for id, entry in database.items():
    if entry['armed'] == 'unarmed':
        unarmed_selection[id] = entry

# Create unarmed_race_counts dictionary
unarmed_race_counts = {}
for entry in unarmed_selection.values():
    race = entry['race']
    unarmed_race_counts[race] = unarmed_race_counts.get(race, 0) + 1

# Calculate and print the fraction of unarmed shootings with a black subject
total_unarmed_shootings = len(unarmed_selection)
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
unarmed_black_fraction = unarmed_black_shootings / total_unarmed_shootings
print(f"Fraction of unarmed shootings with a black subject: {unarmed_black_fraction:.4f}")