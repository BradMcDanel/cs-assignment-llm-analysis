import csv

# Initialize the database dictionary
database = {}

# Read the data from the CSV file and populate the database dictionary
with open('fatal-police-shootings-data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Use the 'id' column as the key for the dictionary
        key = row['id']
        # Store the rest of the data as a dictionary
        database[key] = {
            'name': row['name'],
            'date': row['date'],
            'manner_of_death': row['manner_of_death'],
            'armed': row['armed'],
            'age': row['age'],
            'gender': row['gender'],
            'race': row['race'],
            'city': row['city'],
            'state': row['state'],
            'signs_of_mental_illness': row['signs_of_mental_illness'] == 'True',
            'threat_level': row['threat_level'],
            'flee': row['flee'],
            'body_camera': row['body_camera'] == 'True',
            'latitude': float(row['latitude']) if row['latitude'] else None,
            'longitude': float(row['longitude']) if row['longitude'] else None,
            'is_geocoding_exact': row['is_geocoding_exact'] == 'True'
        }

# Task 3: Analyzing the data

# Print the name of the subject with ID number 1694
print(database['1694']['name'])

# Print the names of all subjects of fatal police shootings in Minnesota
for key, value in database.items():
    if value['state'] == 'MN':
        print(value['name'])

# Create a dictionary to count the occurrences of each race
race_counts = {}
for key, value in database.items():
    race = value['race']
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Print the fraction of fatal police shootings with a black subject
total_shootings = len(database)
black_shootings = race_counts.get('B', 0)
print(black_shootings / total_shootings)

# Create a dictionary to store unarmed fatal police shootings
unarmed_selection = {}
for key, value in database.items():
    if value['armed'] == 'unarmed':
        unarmed_selection[key] = value

# Create a dictionary to count the occurrences of each race in unarmed shootings
unarmed_race_counts = {}
for key, value in unarmed_selection.items():
    race = value['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Print the fraction of unarmed fatal police shootings with a black subject
total_unarmed_shootings = len(unarmed_selection)
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
print(unarmed_black_shootings / total_unarmed_shootings)