# Open the CSV file containing the fatal police shootings data
data_file = open("fatal-police-shootings-data.csv", 'r')
data_lines = data_file.readlines()

# Initialize an empty dictionary to store the database
database = {}

# Iterate through each line of the CSV file (skipping the header)
for row in range(1, len(data_lines)):
    line = data_lines[row]
    entries = line.split(',')
    db_entry = {}
    
    # Extract relevant information and store it in the db_entry dictionary
    db_entry["name"] = entries[11]
    db_entry["date"] = entries[1]
    db_entry["armed"] = entries[4]
    db_entry["age"] = entries[12]
    db_entry["gender"] = entries[13]
    db_entry["race"] = entries[14]
    db_entry["state"] = entries[8]
    
    # Use the ID as the key for the database dictionary
    entry_id = int(entries[0])
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