# Existing code (provided)
data_file = open("fatal-police-shootings-data.csv", 'r')
data_lines = data_file.readlines()

database = {}
for row in range(1, len(data_lines)):
    line = data_lines[row]
    entries = line.split(',')
    db_entry = {}
    db_entry["name"] = entries[11]
    db_entry["date"] = entries[1]
    db_entry["armed"] = entries[4]
    db_entry["age"] = entries[12]
    db_entry["gender"] = entries[13]
    db_entry["race"] = entries[14]
    db_entry["state"] = entries[8]
    entry_id = int(entries[0])
    database[entry_id] = db_entry

# New code for Task 3

# Print name of subject with ID 1694
print(f"Subject with ID 1694: {database[1694]['name']}")

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

# Print fraction of shootings with black subjects
total_shootings = len(database)
black_shootings = race_counts.get('B', 0)
black_fraction = black_shootings / total_shootings
print(f"Fraction of shootings with black subjects: {black_fraction:.4f}")

# Create unarmed_selection dictionary
unarmed_selection = {id: entry for id, entry in database.items() if entry['armed'] == 'unarmed'}

# Create unarmed_race_counts dictionary
unarmed_race_counts = {}
for entry in unarmed_selection.values():
    race = entry['race']
    unarmed_race_counts[race] = unarmed_race_counts.get(race, 0) + 1

# Print fraction of unarmed shootings with black subjects
total_unarmed_shootings = len(unarmed_selection)
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
unarmed_black_fraction = unarmed_black_shootings / total_unarmed_shootings
print(f"Fraction of unarmed shootings with black subjects: {unarmed_black_fraction:.4f}")