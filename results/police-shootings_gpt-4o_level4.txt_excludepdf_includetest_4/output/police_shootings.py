import csv

# Step 1: Read data from CSV and create the 'database' dictionary
database = {}

# Open the CSV file and parse it
with open('fatal-police-shootings-data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Extract the ID as the key
        key = int(row['id'])
        # Store the row data in the database with the ID as the key
        database[key] = row

# Task 3: Additional code to perform the required analysis

# Print the name of the subject of the fatal police shooting with ID number 1694
subject_id_1694 = database[1694]['name']
print(f"Name of subject with ID 1694: {subject_id_1694}")

# Print the names of all subjects of fatal police shootings in Minnesota
print("Names of subjects of fatal police shootings in Minnesota:")
for data in database.values():
    if data['state'] == 'MN':
        print(data['name'])

# Create a dictionary to count the occurrences of races
race_counts = {}
for data in database.values():
    race = data['race']
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Print the fraction of fatal police shootings with a black subject
black_shootings = race_counts.get('B', 0)
total_shootings = len(database)
black_shooting_fraction = black_shootings / total_shootings
print(f"Fraction of fatal police shootings with a black subject: {black_shooting_fraction}")

# Create a dictionary of unarmed fatal police shootings
unarmed_selection = {}
for key, data in database.items():
    if data['armed'] == 'unarmed':
        unarmed_selection[key] = data

# Create a dictionary to count the occurrences of races in unarmed selection
unarmed_race_counts = {}
for data in unarmed_selection.values():
    race = data['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Print the fraction of unarmed fatal police shootings with a black subject
black_unarmed_shootings = unarmed_race_counts.get('B', 0)
total_unarmed_shootings = len(unarmed_selection)
black_unarmed_shooting_fraction = black_unarmed_shootings / total_unarmed_shootings
print(f"Fraction of unarmed fatal police shootings with a black subject: {black_unarmed_shooting_fraction}")