import csv

# Initialize an empty dictionary to store the data
database = {}

# Open the CSV file and read its contents
with open('fatal-police-shootings-data.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Iterate through each row in the CSV file
    for row in reader:
        # Extract the relevant information from the row
        id = row['id']
        name = row['name']
        date = row['date']
        manner_of_death = row['manner_of_death']
        armed = row['armed']
        age = row['age']
        gender = row['gender']
        race = row['race']
        city = row['city']
        state = row['state']
        
        # Create a dictionary with the extracted information
        entry = {
            'name': name,
            'date': date,
            'manner_of_death': manner_of_death,
            'armed': armed,
            'age': age,
            'gender': gender,
            'race': race,
            'city': city,
            'state': state
        }
        
        # Add the entry to the database, using the ID as the key
        database[id] = entry

# Task 3: Using the database

# Print the name of the subject with ID number 1694
print(f"Name of subject with ID 1694: {database['1694']['name']}")

# Print names of all subjects in Minnesota
print("Names of subjects in Minnesota:")
for id, data in database.items():
    if data['state'] == 'MN':
        print(data['name'])

# Create race_counts dictionary
race_counts = {}
for data in database.values():
    race = data['race']
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Print fraction of fatal police shootings with a black subject
total_shootings = len(database)
black_shootings = race_counts.get('B', 0)
fraction_black = black_shootings / total_shootings
print(f"Fraction of fatal police shootings with a black subject: {fraction_black:.4f}")

# Create unarmed_selection dictionary
unarmed_selection = {}
for id, data in database.items():
    if data['armed'] == 'unarmed':
        unarmed_selection[id] = data

# Create unarmed_race_counts dictionary
unarmed_race_counts = {}
for data in unarmed_selection.values():
    race = data['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Print fraction of unarmed fatal police shootings with a black subject
total_unarmed_shootings = len(unarmed_selection)
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
fraction_unarmed_black = unarmed_black_shootings / total_unarmed_shootings
print(f"Fraction of unarmed fatal police shootings with a black subject: {fraction_unarmed_black:.4f}")