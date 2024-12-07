data_file = open("fatal-police-shootings-data.csv", 'r')
data_lines = data_file.readlines()

# Initializing the database dictionary
database = {}
# Looping through each line in the data file, starting from the second line
for row in range(1, len(data_lines)):
    line = data_lines[row]
    # Splitting the line by comma to separate each data entry
    entries = line.split(',')
    # Constructing a dictionary for each entry
    db_entry = {}
    db_entry["name"] = entries[1]
    db_entry["date"] = entries[2]
    db_entry["armed"] = entries[4]
    db_entry["age"] = entries[5]
    db_entry["gender"] = entries[6]
    db_entry["race"] = entries[7]
    db_entry["state"] = entries[9]
    entry_id = int(entries[0])  # Using the ID as the key in the database
    database[entry_id] = db_entry

# Task 3: Find the name of the person with ID 1694
print("Name with ID 1694:", database[1694]["name"])

# Task 3: Print all names of subjects in Minnesota
print("Names of subjects in Minnesota:")
for entry_id, details in database.items():
    if details["state"] == "MN":
        print(details["name"])

# Task 3: Create race_counts dictionary
race_counts = {}
for entry_id, details in database.items():
    race = details["race"]
    if race not in race_counts:
        race_counts[race] = 0
    race_counts[race] += 1

# Print proportions
total_shootings = len(database)
black_shootings = race_counts.get("B", 0)
print("Proportion of black subjects:", black_shootings / total_shootings)

# Task 3: Unarmed dictionary and calculations
unarmed_selection = {}
for entry_id, details in database.items():
    if details["armed"].lower() == "unarmed":
        unarmed_selection[entry_id] = details

unarmed_race_counts = {}
for entry_id, details in unarmed_selection.items():
    race = details["race"]
    if race not in unarmed_race_counts:
        unarmed_race_counts[race] = 0
    unarmed_race_counts[race] += 1

total_unarmed_shootings = len(unarmed_selection)
black_unarmed_shootings = unarmed_race_counts.get("B", 0)
print("Proportion of unarmed black subjects:", black_unarmed_shootings / total_unarmed_shootings)