import csv

# Step 1: Read the CSV file and create a database dictionary
database = {}
with open('fatal-police-shootings-data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Assuming 'id' is a unique identifier for each shooting incident
        database[row['id']] = row

# Task 3: Using the database to answer questions
# Print the name of the subject of the fatal police shooting with ID number 1694.
print("Name of subject with ID 1694:", database['1694']['name'])

# Print the names of all subjects of fatal police shootings in Minnesota
print("Subjects of fatal police shootings in Minnesota:")
for data in database.values():
    if data['state'] == 'MN':
        print(data['name'])

# Create a new dictionary to count occurrences of each race
race_counts = {}
for data in database.values():
    race = data['race']
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Print the fraction of fatal police shootings with a black subject
total_shootings = len(database)
black_shootings = race_counts.get('B', 0)
fraction_black_shootings = black_shootings / total_shootings
print("Fraction of fatal police shootings with a black subject:", fraction_black_shootings)

# Create a new dictionary for unarmed selection
unarmed_selection = {}
for key, data in database.items():
    if data['armed'] == 'unarmed':
        unarmed_selection[key] = data

# Create a new dictionary to count races among unarmed shootings
unarmed_race_counts = {}
for data in unarmed_selection.values():
    race = data['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Print the fraction of unarmed fatal police shootings with a black subject
total_unarmed_shootings = len(unarmed_selection)
black_unarmed_shootings = unarmed_race_counts.get('B', 0)
fraction_black_unarmed_shootings = black_unarmed_shootings / total_unarmed_shootings
print("Fraction of unarmed fatal police shootings with a black subject:", fraction_black_unarmed_shootings)