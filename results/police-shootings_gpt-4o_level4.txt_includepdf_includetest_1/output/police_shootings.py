# Open and read data from the CSV file
data_file = open("fatal-police-shootings-data.csv", 'r')
data_lines = data_file.readlines()

# Initialize the database dictionary
database = {}
for row in range(1, len(data_lines)):
    # Split each line into components
    line = data_lines[row]
    entries = line.split(',')
    
    # Create a dictionary for each entry
    db_entry = {}
    db_entry["name"] = entries[11]
    db_entry["date"] = entries[1]
    db_entry["armed"] = entries[4]
    db_entry["age"] = entries[12]
    db_entry["gender"] = entries[13]
    db_entry["race"] = entries[14]
    db_entry["state"] = entries[7]
    
    # Use the ID as key in the database dictionary
    entry_id = int(entries[0])
    database[entry_id] = db_entry

# Task 3 implementation
# 1. Print the name of the subject of the fatal police shooting with ID number 1694
print(database[1694]["name"])

# 2. Print the names of all subjects of fatal police shootings in Minnesota
for entry_id, entry in database.items():
    if entry["state"] == "MN":
        print(entry["name"])

# 3. Create a race counts dictionary
race_counts = {}
for entry in database.values():
    race = entry["race"]
    if race not in race_counts:
        race_counts[race] = 0
    race_counts[race] += 1

# 4. Print the fraction of fatal police shootings with a black subject
black_shootings = race_counts.get("B", 0)
total_shootings = len(database)
print(black_shootings / total_shootings)

# Additional task: Analyze unarmed shootings
unarmed_selection = {}
for entry_id, entry in database.items():
    if entry["armed"].lower() == "unarmed":
        unarmed_selection[entry_id] = entry

# Create unarmed race counts dictionary
unarmed_race_counts = {}
for entry in unarmed_selection.values():
    race = entry["race"]
    if race not in unarmed_race_counts:
        unarmed_race_counts[race] = 0
    unarmed_race_counts[race] += 1

# Print the fraction of unarmed fatal police shootings with a black subject
unarmed_black_shootings = unarmed_race_counts.get("B", 0)
total_unarmed_shootings = len(unarmed_selection)
print(unarmed_black_shootings / total_unarmed_shootings)