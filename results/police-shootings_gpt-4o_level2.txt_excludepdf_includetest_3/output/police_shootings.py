# Print the name of the subject with ID number 1694
print("Name of subject with ID 1694:", database['1694']['name'])

# Print the names of all subjects of fatal police shootings in Minnesota
print("Subjects of fatal police shootings in Minnesota:")
for entry in database.values():
    if entry['state'] == 'MN':
        print(entry['name'])

# Create a dictionary to count occurrences of each race
race_counts = {}
for entry in database.values():
    race = entry['race']
    race_counts[race] = race_counts.get(race, 0) + 1

# Print the fraction of fatal police shootings with a black subject
total_shootings = len(database)
black_shootings = race_counts.get('B', 0)
fraction_black_shootings = black_shootings / total_shootings
print("Fraction of fatal police shootings with a black subject:", fraction_black_shootings)

# Create a dictionary for unarmed shootings
unarmed_selection = {key: value for key, value in database.items() if value['armed'] == 'unarmed'}

# Create a dictionary to count occurrences of each race in unarmed shootings
unarmed_race_counts = {}
for entry in unarmed_selection.values():
    race = entry['race']
    unarmed_race_counts[race] = unarmed_race_counts.get(race, 0) + 1

# Print the fraction of unarmed fatal police shootings with a black subject
total_unarmed_shootings = len(unarmed_selection)
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
fraction_unarmed_black_shootings = unarmed_black_shootings / total_unarmed_shootings
print("Fraction of unarmed fatal police shootings with a black subject:", fraction_unarmed_black_shootings)