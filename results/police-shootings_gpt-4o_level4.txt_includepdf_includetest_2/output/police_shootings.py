data_file = open("fatal-police-shootings-data.csv", 'r')
data_lines = data_file.readlines()

database = {}
for row in range(1, len(data_lines)):
    line = data_lines[row]
    entries = line.split(',')
    db_entry = {}
    db_entry["name"] = entries[12]
    db_entry["date"] = entries[1]
    db_entry["armed"] = entries[4]
    db_entry["age"] = entries[13]
    db_entry["gender"] = entries[14]
    db_entry["race"] = entries[15]
    db_entry["state"] = entries[9]
    entry_id = int(entries[0])
    database[entry_id] = db_entry

# Task 3 code starts here

# Print the name of the subject of the fatal police shooting with ID number 1694
print(database[1694]["name"])

# Print the name of all subjects of fatal police shootings in Minnesota
for key, value in database.items():
    if value["state"] == "MN":
        print(value["name"])

# Create a new dictionary, race_counts, to count occurrences of each race
race_counts = {}
for key, value in database.items():
    race = value["race"]
    if race not in race_counts:
        race_counts[race] = 0
    race_counts[race] += 1

# Print the fraction of fatal police shootings with a black subject
total_shootings = len(database)
black_shootings = race_counts.get("B", 0)
print(black_shootings / total_shootings)

# Create a new dictionary, unarmed_selection, for unarmed fatal police shootings
unarmed_selection = {}
for key, value in database.items():
    if value["armed"] == "unarmed":
        unarmed_selection[key] = value

# Create a new dictionary, unarmed_race_counts, to count occurrences of each race among unarmed subjects
unarmed_race_counts = {}
for key, value in unarmed_selection.items():
    race = value["race"]
    if race not in unarmed_race_counts:
        unarmed_race_counts[race] = 0
    unarmed_race_counts[race] += 1

# Print the fraction of unarmed fatal police shootings with a black subject
total_unarmed_shootings = len(unarmed_selection)
black_unarmed_shootings = unarmed_race_counts.get("B", 0)
print(black_unarmed_shootings / total_unarmed_shootings)