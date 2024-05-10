from police_shootings import database

# Print the name of the subject with ID number 1694
print(database[1694]['name'])

# Print the names of all subjects in Minnesota
for key, value in database.items():
    if value['state'] == 'MN':
        print(value['name'])

# Create race_counts dictionary to count occurrences of each race
race_counts = {}
for key, value in database.items():
    race = value['race']
    race_counts[race] = race_counts.get(race, 0) + 1

# Calculate and print the fraction of fatal police shootings with a black subject
total_shootings = len(database)
black_shootings = race_counts.get('B', 0)
fraction_black_shootings = black_shootings / total_shootings
print(fraction_black_shootings)