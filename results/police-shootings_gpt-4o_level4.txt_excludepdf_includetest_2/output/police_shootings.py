import csv

# Open the CSV file containing the data on fatal police shootings
with open('fatal-police-shootings-data.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    # Initialize an empty dictionary to store the data
    database = {}
    
    # Iterate through each row in the CSV reader
    for row in reader:
        # Use the 'id' field as the key in the dictionary
        key = int(row['id'])
        # Store the entire row as the value in the dictionary
        database[key] = row

# Task 3: Extend the code to analyze the data

# Print the name of the subject of the fatal police shooting with ID number 1694
print("Subject of fatal shooting with ID 1694:", database[1694]['name'])

# Print the names of all subjects of fatal police shootings in Minnesota
print("Subjects of fatal shootings in Minnesota:")
for record in database.values():
    if record['state'] == 'MN':
        print(record['name'])

# Create a dictionary to count occurrences of each race
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
black_fraction = black_shootings / total_shootings
print("Fraction of fatal police shootings with a black subject:", black_fraction)

# Filter for unarmed subjects and create a new dictionary
unarmed_selection = {k: v for k, v in database.items() if v['armed'] == 'unarmed'}

# Create a dictionary to count occurrences of each race among unarmed subjects
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
unarmed_black_fraction = unarmed_black_shootings / total_unarmed_shootings
print("Fraction of unarmed fatal police shootings with a black subject:", unarmed_black_fraction)