# Existing code to read data and create database (unchanged)
data_file = open("fatal-police-shootings-data.csv", 'r')
data_lines = data_file.readlines()

database = {}
for row in range(1, len(data_lines)):
    line = data_lines[row]
    entries = line.split(',')
    db_entry = {}
    db_entry["name"] = entries[1]
    db_entry["date"] = entries[2]
    db_entry["armed"] = entries[4]
    db_entry["age"] = entries[5]
    db_entry["gender"] = entries[6]
    db_entry["race"] = entries[7]
    db_entry["state"] = entries[9]
    entry_id = int(entries[0])
    database[entry_id] = db_entry

# Print name of subject with ID 1694
print(f"Name of subject with ID 1694: {database[1694]['name']}")

# Print names of all subjects in Minnesota
print("Names of subjects in Minnesota:")
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

# Print fraction of shootings with a black subject
total_shootings = sum(race_counts.values())
black_shootings = race_counts.get('B', 0)
black_fraction = black_shootings / total_shootings
print(f"Fraction of shootings with a black subject: {black_fraction:.4f}")

# Create unarmed_selection dictionary
unarmed_selection = {}
for id, entry in database.items():
    if entry['armed'] == 'unarmed':
        unarmed_selection[id] = entry

# Create unarmed_race_counts dictionary
unarmed_race_counts = {}
for entry in unarmed_selection.values():
    race = entry['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Print fraction of unarmed shootings with a black subject
total_unarmed_shootings = sum(unarmed_race_counts.values())
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
unarmed_black_fraction = unarmed_black_shootings / total_unarmed_shootings
print(f"Fraction of unarmed shootings with a black subject: {unarmed_black_fraction:.4f}")