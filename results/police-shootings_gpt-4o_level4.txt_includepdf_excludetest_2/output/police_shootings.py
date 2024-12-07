# Open the data file
data_file = open("fatal-police-shootings-data.csv", 'r')
data_lines = data_file.readlines()

# Initialize an empty dictionary to store the data
database = {}

# Iterate through each line in the data file starting from the second line
for row in range(1, len(data_lines)):
    line = data_lines[row]
    entries = line.split(',')
    
    # Create a dictionary for each entry with relevant information
    db_entry = {}
    db_entry["name"] = entries[11]
    db_entry["date"] = entries[1]
    db_entry["armed"] = entries[4]
    db_entry["age"] = entries[12]
    db_entry["gender"] = entries[13]
    db_entry["race"] = entries[14]
    db_entry["state"] = entries[8]
    
    # Use the ID as the key in the database dictionary
    entry_id = int(entries[0])
    database[entry_id] = db_entry

# Task 3: Additional Code

# Print the name of the subject of the fatal police shooting with ID number 1694
print("Subject with ID 1694:", database[1694]["name"])

# Print the names of all subjects of fatal police shootings in Minnesota
print("Subjects of fatal police shootings in Minnesota:")
for entry_id, info in database.items():
    if info["state"] == "MN":
        print(info["name"])

# Create a new dictionary to count occurrences of each race
race_counts = {}
for entry_id, info in database.items():
    race = info["race"]
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Print the fraction of fatal police shootings with a black subject
total_shootings = len(database)
black_shootings = race_counts.get("B", 0)
fraction_black = black_shootings / total_shootings
print("Fraction of fatal police shootings with a black subject:", fraction_black)

# Create a new dictionary for unarmed selections
unarmed_selection = {}
for entry_id, info in database.items():
    if info["armed"].strip() == "unarmed":
        unarmed_selection[entry_id] = info

# Create a new dictionary to count unarmed race occurrences
unarmed_race_counts = {}
for entry_id, info in unarmed_selection.items():
    race = info["race"]
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Print the fraction of unarmed fatal police shootings with a black subject
total_unarmed_shootings = len(unarmed_selection)
unarmed_black_shootings = unarmed_race_counts.get("B", 0)
fraction_unarmed_black = unarmed_black_shootings / total_unarmed_shootings
print("Fraction of unarmed fatal police shootings with a black subject:", fraction_unarmed_black)