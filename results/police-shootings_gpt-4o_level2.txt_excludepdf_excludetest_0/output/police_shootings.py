# Continued from previous code

# Find and print the name of the subject with ID number 1694
print(database['1694']['name'])

# Print names of all subjects of fatal police shootings in Minnesota
for key, value in database.items():
    if value['state'] == 'MN':
        print(value['name'])

# Create dictionary to count occurrences of each race
race_counts = {}
for key, value in database.items():
    race = value['race']
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Calculate and print the fraction of shootings with a black subject
black_shootings = race_counts.get('B', 0)
total_shootings = len(database)
fraction_black = black_shootings / total_shootings
print(fraction_black)

# Question 1: The proportion of black subjects in fatal police shootings is higher than their representation in the general United States population, which is 14%.

# Create dictionary for unarmed shootings
unarmed_selection = {}
for key, value in database.items():
    if value['armed'] == 'unarmed':
        unarmed_selection[key] = value

# Create dictionary to count race occurrences in unarmed shootings
unarmed_race_counts = {}
for key, value in unarmed_selection.items():
    race = value['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Calculate and print the fraction of unarmed shootings with a black subject
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
total_unarmed_shootings = len(unarmed_selection)
fraction_unarmed_black = unarmed_black_shootings / total_unarmed_shootings
print(fraction_unarmed_black)

# Question 2: The proportion of black subjects in unarmed fatal police shootings is also higher than their representation in the general population, similar to the overall findings for all police shootings.