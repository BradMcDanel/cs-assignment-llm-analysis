import csv

# Initialize an empty dictionary to store the data
database = {}

# Open the CSV file and read its content
with open('fatal-police-shootings-data.csv', newline='') as csvfile:
    # Use csv.DictReader to read the CSV into a dictionary format
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Use the 'id' column as the key for the database dictionary
        key = row['id']
        # Store the entire row (as a dictionary) as the value for this key
        database[key] = row

# Task 3: Extended functionality starts here

# Print the name of the subject with ID 1694
subject_id = '1694'
if subject_id in database:
    print(f"Subject with ID {subject_id}: {database[subject_id]['name']}")

# Print all subjects of fatal police shootings in Minnesota
print("Subjects of fatal shootings in Minnesota:")
for entry in database.values():
    if entry['state'] == 'MN':
        print(entry['name'])

# Create race_counts dictionary
race_counts = {}
for entry in database.values():
    race = entry['race']
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Calculate the fraction of black subjects
black_shootings = race_counts.get('B', 0)
total_shootings = len(database)
fraction_black = black_shootings / total_shootings
print(f"Fraction of fatal police shootings with a black subject: {fraction_black:.2f}")

# Create unarmed_selection dictionary
unarmed_selection = {k: v for k, v in database.items() if v['armed'] == 'unarmed'}

# Create unarmed_race_counts dictionary
unarmed_race_counts = {}
for entry in unarmed_selection.values():
    race = entry['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Calculate the fraction of unarmed black subjects
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
total_unarmed_shootings = len(unarmed_selection)
fraction_unarmed_black = unarmed_black_shootings / total_unarmed_shootings
print(f"Fraction of unarmed fatal police shootings with a black subject: {fraction_unarmed_black:.2f}")