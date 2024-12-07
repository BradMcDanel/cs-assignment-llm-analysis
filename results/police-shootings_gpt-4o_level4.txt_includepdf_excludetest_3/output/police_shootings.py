# Open the CSV file containing the data on fatal police shootings
data_file = open("fatal-police-shootings-data.csv", 'r')

# Read all lines from the file
data_lines = data_file.readlines()

# Initialize an empty dictionary to store the data
database = {}

# Iterate over each line in the data file, starting from the second line
# because the first line contains headers
for row in range(1, len(data_lines)):
    line = data_lines[row]  # Get the current line
    entries = line.split(',')  # Split the line by commas to get individual entries

    # Create a dictionary for each entry
    db_entry = {}
    db_entry["name"] = entries[11]  # Name of the individual
    db_entry["date"] = entries[1]   # Date of the incident
    db_entry["armed"] = entries[4]  # Whether the individual was armed
    db_entry["age"] = entries[12]   # Age of the individual
    db_entry["gender"] = entries[13]  # Gender of the individual
    db_entry["race"] = entries[14]  # Race of the individual
    db_entry["state"] = entries[8]  # State where the incident occurred

    # Use the unique ID as the key for the database dictionary
    entry_id = int(entries[0])
    database[entry_id] = db_entry  # Store the entry in the database

# Task 3: Using the database

# Print the name of the subject of the fatal police shooting with ID number 1694
print(f"Name of subject with ID 1694: {database[1694]['name']}")

# Print the name of all subjects of fatal police shootings in Minnesota
print("Subjects of fatal police shootings in Minnesota:")
for entry_id, entry in database.items():
    if entry["state"] == "MN":
        print(entry["name"])

# Create a dictionary to count occurrences of each race
race_counts = {}
for entry in database.values():
    race = entry["race"]
    if race not in race_counts:
        race_counts[race] = 0
    race_counts[race] += 1

# Calculate and print the fraction of fatal police shootings with a black subject
black_shootings = race_counts.get('B', 0)
total_shootings = len(database)
fraction_black = black_shootings / total_shootings
print(f"Fraction of fatal police shootings with a black subject: {fraction_black}")

# Restrict to unarmed subjects
unarmed_selection = {}
for entry_id, entry in database.items():
    if entry["armed"] == "unarmed":
        unarmed_selection[entry_id] = entry

# Create a dictionary to count occurrences of each race among unarmed subjects
unarmed_race_counts = {}
for entry in unarmed_selection.values():
    race = entry["race"]
    if race not in unarmed_race_counts:
        unarmed_race_counts[race] = 0
    unarmed_race_counts[race] += 1

# Calculate and print the fraction of unarmed fatal police shootings with a black subject
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
total_unarmed_shootings = len(unarmed_selection)
fraction_unarmed_black = unarmed_black_shootings / total_unarmed_shootings
print(f"Fraction of unarmed fatal police shootings with a black subject: {fraction_unarmed_black}")