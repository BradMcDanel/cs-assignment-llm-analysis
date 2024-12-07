# Import necessary modules
import csv

# Read the CSV file and create the database dictionary
data_file = open("fatal-police-shootings-data.csv", 'r')
csv_reader = csv.DictReader(data_file)

database = {}
for row in csv_reader:
    entry_id = int(row['id'])
    db_entry = {
        "name": row['name'],
        "date": row['date'],
        "armed": row['armed_with'],
        "age": row['age'],
        "gender": row['gender'],
        "race": row['race'],
        "state": row['state']
    }
    database[entry_id] = db_entry

# Task 3: Using the database

# Print the name of the subject with ID number 1694
print(f"Subject with ID 1694: {database[1694]['name']}")

# Print names of all subjects in Minnesota
print("\nSubjects in Minnesota:")
for entry in database.values():
    if entry['state'] == 'MN':
        print(entry['name'])

# Create race_counts dictionary
race_counts = {}
for entry in database.values():
    race = entry['race']
    race_counts[race] = race_counts.get(race, 0) + 1

# Calculate and print the fraction of fatal police shootings with a black subject
total_shootings = sum(race_counts.values())
black_shootings = race_counts.get('B', 0)
black_fraction = black_shootings / total_shootings
print(f"\nFraction of fatal police shootings with a black subject: {black_fraction:.3f}")

# Create unarmed_selection dictionary
unarmed_selection = {id: entry for id, entry in database.items() if entry['armed'] == 'unarmed'}

# Create unarmed_race_counts dictionary
unarmed_race_counts = {}
for entry in unarmed_selection.values():
    race = entry['race']
    unarmed_race_counts[race] = unarmed_race_counts.get(race, 0) + 1

# Calculate and print the fraction of unarmed fatal police shootings with a black subject
total_unarmed_shootings = sum(unarmed_race_counts.values())
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
unarmed_black_fraction = unarmed_black_shootings / total_unarmed_shootings
print(f"Fraction of unarmed fatal police shootings with a black subject: {unarmed_black_fraction:.3f}")