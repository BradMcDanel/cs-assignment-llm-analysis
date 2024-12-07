# Open the data file containing information about fatal police shootings
data_file = open("fatal-police-shootings-data.csv", 'r')

# Read all lines from the file into a list
data_lines = data_file.readlines()

# Initialize an empty dictionary to store the data
database = {}

# Iterate over each line in the data file (skip the header line)
for row in range(1, len(data_lines)):
    line = data_lines[row]  # Get the current line
    entries = line.split(',')  # Split the line by commas to get individual fields
    
    # Create a dictionary for each database entry with relevant information
    db_entry = {}
    db_entry["name"] = entries[11]  # Subject's name
    db_entry["date"] = entries[1]  # Date of the incident
    db_entry["armed"] = entries[4]  # Whether the subject was armed
    db_entry["age"] = entries[12]  # Age of the subject
    db_entry["gender"] = entries[13]  # Gender of the subject
    db_entry["race"] = entries[14]  # Race of the subject
    db_entry["state"] = entries[8]  # State where the incident occurred

    # Use the ID as the key for the entry in the database
    entry_id = int(entries[0])
    database[entry_id] = db_entry

# Task 3: Additional Code
# Print the name of the subject of the fatal police shooting with ID number 1694
if 1694 in database:
    print("Name of subject with ID 1694:", database[1694]["name"])

# Print the names of all subjects of fatal police shootings in Minnesota
print("Subjects of fatal police shootings in Minnesota:")
for entry_id, entry in database.items():
    if entry["state"] == "MN":
        print(entry["name"])

# Create a dictionary to count occurrences of each race
race_counts = {}
for entry in database.values():
    race = entry["race"]
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Print the fraction of fatal police shootings with a black subject
black_shootings = race_counts.get("B", 0)
total_shootings = len(database)
print("Fraction of fatal police shootings with a black subject:", black_shootings / total_shootings)

# Create a dictionary for shootings where the subject was unarmed
unarmed_selection = {entry_id: entry for entry_id, entry in database.items() if entry["armed"] == "unarmed"}

# Create a dictionary to count occurrences of each race among unarmed subjects
unarmed_race_counts = {}
for entry in unarmed_selection.values():
    race = entry["race"]
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Print the fraction of unarmed fatal police shootings with a black subject
black_unarmed_shootings = unarmed_race_counts.get("B", 0)
total_unarmed_shootings = len(unarmed_selection)
print("Fraction of unarmed fatal police shootings with a black subject:", black_unarmed_shootings / total_unarmed_shootings)