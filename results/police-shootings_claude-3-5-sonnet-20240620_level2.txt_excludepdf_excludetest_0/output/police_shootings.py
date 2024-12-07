# [Previous code remains unchanged]

# Print the name of the subject with ID number 1694
print(f"The subject with ID 1694 is: {database['1694']['name']}")

# Print names of all subjects in Minnesota
print("Subjects of fatal police shootings in Minnesota:")
for id, data in database.items():
    if data['state'] == 'MN':
        print(data['name'])

# Create race_counts dictionary
race_counts = {}
for data in database.values():
    race = data['race']
    race_counts[race] = race_counts.get(race, 0) + 1

# Calculate and print fraction of shootings with a black subject
total_shootings = len(database)
black_shootings = race_counts.get('B', 0)
black_fraction = black_shootings / total_shootings
print(f"Fraction of fatal police shootings with a black subject: {black_fraction:.4f}")

# Create unarmed_selection dictionary
unarmed_selection = {id: data for id, data in database.items() if data['armed'] == 'unarmed'}

# Create unarmed_race_counts dictionary
unarmed_race_counts = {}
for data in unarmed_selection.values():
    race = data['race']
    unarmed_race_counts[race] = unarmed_race_counts.get(race, 0) + 1

# Calculate and print fraction of unarmed shootings with a black subject
total_unarmed_shootings = len(unarmed_selection)
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
unarmed_black_fraction = unarmed_black_shootings / total_unarmed_shootings
print(f"Fraction of unarmed fatal police shootings with a black subject: {unarmed_black_fraction:.4f}")