# Open the CSV data file for reading
data_file = open("fatal-police-shootings-data.csv", 'r')
data_lines = data_file.readlines()

# Initialize an empty dictionary to store the data
database = {}

# Iterate over each line in the CSV file (skipping the header)
for row in range(1, len(data_lines)):
    line = data_lines[row]
    # Split the line by commas to extract individual fields
    entries = line.split(',')
    # Create a dictionary entry for each line with relevant fields
    db_entry = {}
    db_entry["name"] = entries[11]  # Name of the individual
    db_entry["date"] = entries[1]   # Date of the incident
    db_entry["armed"] = entries[4]  # Was the individual armed
    db_entry["age"] = entries[12]   # Age of the individual
    db_entry["gender"] = entries[13] # Gender of the individual
    db_entry["race"] = entries[14]  # Race of the individual
    db_entry["state"] = entries[8]  # State where the incident occurred
    entry_id = int(entries[0])      # ID of the incident
    # Store the entry in the database dictionary
    database[entry_id] = db_entry

# Task 3: Answering questions using the database
# Print the name of the subject with ID 1694
print(database[1694]["name"])

# Print names of all subjects of fatal police shootings in Minnesota
for entry in database.values():
    if entry["state"] == 'MN':
        print(entry["name"])

# Create a dictionary to count occurrences of each race
race_counts = {}
for entry in database.values():
    race = entry["race"]
    if race:  # Check if race information is available
        race_counts[race] = race_counts.get(race, 0) + 1

# Calculate and print the fraction of shootings with a black subject
black_fraction = race_counts.get("B", 0) / len(database)
print(black_fraction)

# Create a dictionary for unarmed selections
unarmed_selection = {}
for key, entry in database.items():
    if entry["armed"] == "unarmed":
        unarmed_selection[key] = entry

# Count the races of unarmed subjects
unarmed_race_counts = {}
for entry in unarmed_selection.values():
    race = entry["race"]
    if race:
        unarmed_race_counts[race] = unarmed_race_counts.get(race, 0) + 1

# Calculate and print the fraction of unarmed shootings with a black subject
unarmed_black_fraction = unarmed_race_counts.get("B", 0) / len(unarmed_selection)
print(unarmed_black_fraction)