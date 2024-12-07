import csv

# Initialize an empty dictionary to store the data
database = {}

# Open the CSV file and read its contents
with open('fatal-police-shootings-data.csv', 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Skip the header row
    next(csv_reader)
    
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Extract relevant information from the row
        id = row[0]
        name = row[1]
        date = row[2]
        manner_of_death = row[3]
        armed = row[4]
        age = row[5]
        gender = row[6]
        race = row[7]
        city = row[8]
        state = row[9]
        
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
        
        # Add the entry to the database dictionary using the ID as the key
        database[id] = entry

# Print the name of the subject with ID number 1694
print(f"Subject with ID 1694: {database['1694']['name']}")

# Print names of all subjects in Minnesota
print("Subjects in Minnesota:")
for id, entry in database.items():
    if entry['state'] == 'MN':
        print(entry['name'])

# Create race_counts dictionary
race_counts = {}
for entry in database.values():
    race = entry['race']
    race_counts[race] = race_counts.get(race, 0) + 1

# Calculate and print the fraction of fatal police shootings with a black subject
total_shootings = len(database)
black_shootings = race_counts.get('B', 0)
black_fraction = black_shootings / total_shootings
print(f"Fraction of fatal police shootings with a black subject: {black_fraction:.4f}")

# Create unarmed_selection dictionary
unarmed_selection = {}
for id, entry in database.items():
    if entry['armed'] == 'unarmed':
        unarmed_selection[id] = entry

# Create unarmed_race_counts dictionary
unarmed_race_counts = {}
for entry in unarmed_selection.values():
    race = entry['race']
    unarmed_race_counts[race] = unarmed_race_counts.get(race, 0) + 1

# Calculate and print the fraction of unarmed fatal police shootings with a black subject
total_unarmed_shootings = len(unarmed_selection)
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
unarmed_black_fraction = unarmed_black_shootings / total_unarmed_shootings
print(f"Fraction of unarmed fatal police shootings with a black subject: {unarmed_black_fraction:.4f}")