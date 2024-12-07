# Open and read the CSV data file
data_file = open("fatal-police-shootings-data.csv", 'r')
data_lines = data_file.readlines()

# Initialize the database as a dictionary
database = {}

# Parsing each line of the CSV starting from the second line (skip header)
for row in range(1, len(data_lines)):
    line = data_lines[row].strip()  # Remove any extraneous whitespace
    entries = line.split(',')  # Split the line into individual data fields
    db_entry = {
        "name": entries[11],  # Name of the subject
        "date": entries[1],  # Date of the incident
        "armed": entries[4],  # Whether the subject was armed
        "age": entries[12],  # Age of the subject
        "gender": entries[13],  # Gender of the subject
        "race": entries[14],  # Race of the subject
        "state": entries[7],  # State where the incident occurred
    }
    entry_id = int(entries[0])  # Unique ID of the incident
    database[entry_id] = db_entry  # Add the entry to the database

# Task: Print the name of the subject with ID 1694
print(database[1694]["name"])

# Task: Print names of all subjects of fatal police shootings in Minnesota
for entry_id, details in database.items():
    if details["state"] == "MN":
        print(details["name"])

# Task: Create race counts dictionary
race_counts = {}
for details in database.values():
    race = details["race"]
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Calculate and print the fraction of fatal police shootings with a black subject
black_fraction = race_counts.get("B", 0) / len(database)
print(black_fraction)

# Task: Create unarmed selection dictionary
unarmed_selection = {entry_id: details for entry_id, details in database.items() if details["armed"] == "unarmed"}

# Task: Create unarmed race counts dictionary
unarmed_race_counts = {}
for details in unarmed_selection.values():
    race = details["race"]
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Calculate and print the fraction of unarmed fatal police shootings with a black subject
unarmed_black_fraction = unarmed_race_counts.get("B", 0) / len(unarmed_selection)
print(unarmed_black_fraction)