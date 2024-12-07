# Print the name of the subject with ID 1694
print(database['1694']['name'])

# Print names of all subjects in Minnesota
for entry in database.values():
    if entry['state'] == 'MN':
        print(entry['name'])

# Create race_counts dictionary
race_counts = {}
for entry in database.values():
    race = entry['race']
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Calculate and print the fraction of fatal shootings with a black subject
black_shootings = race_counts.get('B', 0)
total_shootings = len(database)
print(black_shootings / total_shootings)

# Create unarmed_selection and unarmed_race_counts
unarmed_selection = {key: value for key, value in database.items() if value['armed'] == 'unarmed'}
unarmed_race_counts = {}
for entry in unarmed_selection.values():
    race = entry['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Calculate and print the fraction of unarmed shootings with a black subject
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
total_unarmed_shootings = len(unarmed_selection)
print(unarmed_black_shootings / total_unarmed_shootings)