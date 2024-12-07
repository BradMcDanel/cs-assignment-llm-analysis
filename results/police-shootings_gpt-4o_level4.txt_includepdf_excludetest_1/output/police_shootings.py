# Open the data file in read mode
data_file = open("fatal-police-shootings-data.csv", 'r')

# Read all lines from the file
data_lines = data_file.readlines()

# Initialize an empty dictionary to store the data
database = {}

# Loop over each row in the data starting from the second line
for row in range(1, len(data_lines)):
    line = data_lines[row]  # Get the current line
    entries = line.split(',')  # Split the line by commas to get each entry
    db_entry = {}  # Create a dictionary to hold this entry's data

    # Extract and store relevant information from the entries into the db_entry
    db_entry["name"] = entries[1]
    db_entry["date"] = entries[2]
    db_entry["armed"] = entries[4]
    db_entry["age"] = entries[5]
    db_entry["gender"] = entries[6]
    db_entry["race"] = entries[7]
    db_entry["state"] = entries[9]

    # Use the ID as the key for the database dictionary
    entry_id = int(entries[0])
    database[entry_id] = db_entry

# Task 3 code starts here:
# Retrieve and print the name of the subject with ID number 1694
print("Name of the subject with ID 1694:", database[1694]["name"])

# Print the names of all subjects of fatal police shootings in Minnesota
print("Names of subjects in Minnesota:")
for entry_id, info in database.items():
    if info["state"] == "MN":
        print(info["name"])

# Create a race counts dictionary
race_counts = {}
for entry_id, info in database.items():
    race = info["race"]
    if race not in race_counts:
        race_counts[race] = 0
    race_counts[race] += 1

# Calculate and print the fraction of shootings with a black subject
black_shootings = race_counts.get("B", 0)
total_shootings = len(database)
print("Fraction of fatal police shootings with a black subject:", black_shootings / total_shootings)

# Create an unarmed selection dictionary
unarmed_selection = {}
for entry_id, info in database.items():
    if info["armed"] == "unarmed":
        unarmed_selection[entry_id] = info

# Create an unarmed race counts dictionary
unarmed_race_counts = {}
for entry_id, info in unarmed_selection.items():
    race = info["race"]
    if race not in unarmed_race_counts:
        unarmed_race_counts[race] = 0
    unarmed_race_counts[race] += 1

# Calculate and print the fraction of unarmed shootings with a black subject
unarmed_black_shootings = unarmed_race_counts.get("B", 0)
total_unarmed_shootings = len(unarmed_selection)
print("Fraction of unarmed fatal police shootings with a black subject:", unarmed_black_shootings / total_unarmed_shootings)