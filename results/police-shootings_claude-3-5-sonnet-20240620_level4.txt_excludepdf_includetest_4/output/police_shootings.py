import csv

# Initialize an empty dictionary to store the data
database = {}

# Open the CSV file and read its contents
with open('fatal-police-shootings-data.csv', 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(file)
    
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Use the 'id' column as the key for our database dictionary
        key = row['id']
        
        # Create a dictionary to store the relevant information for each shooting
        value = {
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
        
        # Add the key-value pair to our database dictionary
        database[key] = value

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
for value in database.values():
    race = value['race']
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
for value in unarmed_selection.values():
    race = value['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Print fraction of unarmed fatal police shootings with a black subject
total_unarmed_shootings = len(unarmed_selection)
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
unarmed_black_fraction = unarmed_black_shootings / total_unarmed_shootings
print(f"Fraction of unarmed fatal police shootings with a black subject: {unarmed_black_fraction:.4f}")