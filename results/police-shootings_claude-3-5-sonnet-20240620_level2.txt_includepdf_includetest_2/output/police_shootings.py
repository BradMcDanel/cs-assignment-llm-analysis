import csv

# Read the CSV file and create the database
database = {}
with open('fatal-police-shootings-data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        entry_id = int(row['id'])
        database[entry_id] = {
            'name': row['name'],
            'date': row['date'],
            'armed': row['armed_with'],
            'age': row['age'],
            'gender': row['gender'],
            'race': row['race'],
            'state': row['state']
        }

# Print the name of the subject with ID number 1694
print(f"Subject with ID 1694: {database[1694]['name']}")

# Print names of all subjects in Minnesota
print("\nSubjects in Minnesota:")
for entry in database.values():
    if entry['state'] == 'MN':
        print(entry['name'])

# Count occurrences of each race
race_counts = {}
for entry in database.values():
    race = entry['race']
    race_counts[race] = race_counts.get(race, 0) + 1

# Calculate and print the fraction of shootings with a black subject
total_shootings = sum(race_counts.values())
black_shootings = race_counts.get('B', 0)
black_fraction = black_shootings / total_shootings
print(f"\nFraction of fatal police shootings with a black subject: {black_fraction:.3f}")

# Create a dictionary for unarmed shootings
unarmed_selection = {id: entry for id, entry in database.items() if entry['armed'] == 'unarmed'}

# Count occurrences of each race in unarmed shootings
unarmed_race_counts = {}
for entry in unarmed_selection.values():
    race = entry['race']
    unarmed_race_counts[race] = unarmed_race_counts.get(race, 0) + 1

# Calculate and print the fraction of unarmed shootings with a black subject
total_unarmed_shootings = sum(unarmed_race_counts.values())
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
unarmed_black_fraction = unarmed_black_shootings / total_unarmed_shootings
print(f"Fraction of unarmed fatal police shootings with a black subject: {unarmed_black_fraction:.3f}")