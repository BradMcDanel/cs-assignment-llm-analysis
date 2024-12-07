# Print the name of the subject with ID number 1694
print(database[1694]['name'])

# Print the names of subjects of all fatal police shootings in Minnesota
for record in database.values():
    if record['state'] == 'MN':
        print(record['name'])

# Creating the race_counts dictionary
race_counts = {}
for record in database.values():
    race = record['race']
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Calculate and print the fraction of fatal police shootings with a black subject
black_shootings = race_counts.get('B', 0)
total_shootings = len(database)
print(black_shootings / total_shootings)

# Create the unarmed_selection dictionary
unarmed_selection = {}
for key, record in database.items():
    if record['armed'] == 'unarmed':
        unarmed_selection[key] = record

# Create the unarmed_race_counts dictionary
unarmed_race_counts = {}
for record in unarmed_selection.values():
    race = record['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Calculate and print the fraction of unarmed fatal police shootings with a black subject
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
total_unarmed_shootings = len(unarmed_selection)
print(unarmed_black_shootings / total_unarmed_shootings)