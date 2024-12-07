import csv

# Task 2: Reading the data into a dictionary
# Open the CSV file and read its contents
with open('fatal-police-shootings-data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    database = {}
    
    # Iterate over each row in the CSV reader object
    for row in reader:
        # Use the 'id' column as the key for the dictionary
        key = row['id']
        # Store the entire row as the value for this key
        database[key] = row

# Task 3: Using the database
# Print the name of the subject of the fatal police shooting with ID number 1694
subject_1694 = database['1694']['name']
print(f'Name of the subject with ID 1694: {subject_1694}')

# Print the names of all subjects in Minnesota
print('Subjects in Minnesota:')
for entry in database.values():
    if entry['state'] == 'MN':
        print(entry['name'])

# Create a dictionary for race counts
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
black_shooting_fraction = black_shootings / total_shootings
print(f'Fraction of fatal shootings with a black subject: {black_shooting_fraction:.4f}')

# Create a dictionary for unarmed selection
unarmed_selection = {key: value for key, value in database.items() if value['armed'] == 'unarmed'}

# Create a dictionary for unarmed race counts
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
unarmed_black_shooting_fraction = unarmed_black_shootings / total_unarmed_shootings
print(f'Fraction of unarmed shootings with a black subject: {unarmed_black_shooting_fraction:.4f}')