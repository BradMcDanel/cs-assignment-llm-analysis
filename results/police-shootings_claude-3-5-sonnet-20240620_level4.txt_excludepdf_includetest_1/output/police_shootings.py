import csv

# Initialize an empty dictionary to store our data
database = {}

# Open the CSV file
with open('fatal-police-shootings-data.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.DictReader(file)
    
    # Iterate through each row in the CSV file
    for row in reader:
        # Get the ID of the shooting incident
        id = row['id']
        
        # Create a dictionary to store relevant information for this incident
        incident_info = {
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
        
        # Add this incident to our database, using the ID as the key
        database[id] = incident_info

# Task 3: Using the database

# Print the name of the subject with ID number 1694
print(f"The name of the subject with ID 1694 is: {database['1694']['name']}")

# Print the names of all subjects in Minnesota
print("Subjects of fatal police shootings in Minnesota:")
for incident in database.values():
    if incident['state'] == 'MN':
        print(incident['name'])

# Create a dictionary to count occurrences of each race
race_counts = {}
for incident in database.values():
    race = incident['race']
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Calculate and print the fraction of fatal police shootings with a black subject
total_shootings = len(database)
black_shootings = race_counts.get('B', 0)
fraction_black = black_shootings / total_shootings
print(f"Fraction of fatal police shootings with a black subject: {fraction_black:.4f}")

# Create a dictionary for unarmed fatal police shootings
unarmed_selection = {}
for id, incident in database.items():
    if incident['armed'] == 'unarmed':
        unarmed_selection[id] = incident

# Create a dictionary to count occurrences of each race in unarmed shootings
unarmed_race_counts = {}
for incident in unarmed_selection.values():
    race = incident['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Calculate and print the fraction of unarmed fatal police shootings with a black subject
total_unarmed_shootings = len(unarmed_selection)
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
fraction_unarmed_black = unarmed_black_shootings / total_unarmed_shootings
print(f"Fraction of unarmed fatal police shootings with a black subject: {fraction_unarmed_black:.4f}")