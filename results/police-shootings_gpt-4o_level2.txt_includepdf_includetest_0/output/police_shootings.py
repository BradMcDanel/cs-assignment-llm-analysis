# (Existing code here...)

# Task 3: Find and print the name of the subject with ID 1694
id_1694 = 1694
print(f"Name of subject with ID 1694: {database[id_1694]['name']}")

# Print names of all subjects of fatal police shootings in Minnesota
print("Names of subjects in Minnesota:")
for entry_id, entry in database.items():
    if entry['state'] == 'MN':
        print(entry['name'])

# Create a race counts dictionary
race_counts = {}
for entry in database.values():
    race = entry['race']
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Print the fraction of fatal police shootings with a black subject
black_shootings = race_counts.get('B', 0)
total_shootings = len(database)
black_fraction = black_shootings / total_shootings
print(f"Fraction of fatal police shootings with a black subject: {black_fraction}")

# Create a dictionary for unarmed shootings
unarmed_selection = {entry_id: entry for entry_id, entry in database.items() if entry['armed'] == 'unarmed'}

# Create a race count dictionary for unarmed shootings
unarmed_race_counts = {}
for entry in unarmed_selection.values():
    race = entry['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Print the fraction of unarmed fatal police shootings with a black subject
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
total_unarmed_shootings = len(unarmed_selection)
unarmed_black_fraction = unarmed_black_shootings / total_unarmed_shootings
print(f"Fraction of unarmed fatal police shootings with a black subject: {unarmed_black_fraction}")