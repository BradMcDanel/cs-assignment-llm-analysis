# Print the name of the subject with ID number 1694
print("Name of subject with ID 1694:", database['1694']['name'])

# Print the names of all subjects of fatal police shootings in Minnesota
print("Fatal police shootings in Minnesota:")
for data in database.values():
    if data['state'] == 'MN':
        print(data['name'])

# Count occurrences of each race in fatal shootings
race_counts = {}
for data in database.values():
    race = data['race']
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Calculate and print the fraction of shootings with a black subject
total_shootings = len(database)
black_shootings = race_counts.get('B', 0)
fraction_black = black_shootings / total_shootings
print("Fraction of fatal shootings with a black subject:", fraction_black)

# Create a dictionary for unarmed shootings
unarmed_selection = {k: v for k, v in database.items() if v['armed'] == 'unarmed'}

# Count occurrences of each race in unarmed shootings
unarmed_race_counts = {}
for data in unarmed_selection.values():
    race = data['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Calculate and print the fraction of unarmed shootings with a black subject
total_unarmed_shootings = len(unarmed_selection)
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
fraction_unarmed_black = unarmed_black_shootings / total_unarmed_shootings
print("Fraction of unarmed shootings with a black subject:", fraction_unarmed_black)