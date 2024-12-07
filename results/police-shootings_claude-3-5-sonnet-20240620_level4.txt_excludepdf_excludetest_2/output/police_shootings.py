import csv

# Initialize an empty dictionary to store the data
database = {}

# Open and read the CSV file
with open('fatal-police-shootings-data.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Iterate through each row in the CSV file
    for row in reader:
        # Use the 'id' as the key for the database dictionary
        key = row['id']
        
        # Create a dictionary for each entry with selected information
        entry = {
            'name': row['name'],
            'date': row['date'],
            'manner_of_death': row['manner_of_death'],
            'armed': row['armed'],
            'age': row['age'],
            'gender': row['gender'],
            'race': row['race'],
            'city': row['city'],
            'state': row['state'],
            'signs_of_mental_illness': row['signs_of_mental_illness'],
            'threat_level': row['threat_level'],
            'flee': row['flee'],
            'body_camera': row['body_camera']
        }
        
        # Add the entry to the database
        database[key] = entry

# Task 3: Using the database

# Print the name of the subject with ID number 1694
print(f"Subject with ID 1694: {database['1694']['name']}")

# Print names of all subjects in Minnesota
print("Subjects in Minnesota:")
for key, value in database.items():
    if value['state'] == 'MN':
        print(value['name'])

# Create race_counts dictionary
race_counts = {}
for entry in database.values():
    race = entry['race']
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Print fraction of fatal police shootings with a black subject
total_shootings = len(database)
black_shootings = race_counts.get('B', 0)
black_fraction = black_shootings / total_shootings
print(f"Fraction of fatal police shootings with a black subject: {black_fraction:.4f}")

# Create unarmed_selection dictionary
unarmed_selection = {}
for key, value in database.items():
    if value['armed'] == 'unarmed':
        unarmed_selection[key] = value

# Create unarmed_race_counts dictionary
unarmed_race_counts = {}
for entry in unarmed_selection.values():
    race = entry['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Print fraction of unarmed fatal police shootings with a black subject
total_unarmed_shootings = len(unarmed_selection)
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
unarmed_black_fraction = unarmed_black_shootings / total_unarmed_shootings
print(f"Fraction of unarmed fatal police shootings with a black subject: {unarmed_black_fraction:.4f}")