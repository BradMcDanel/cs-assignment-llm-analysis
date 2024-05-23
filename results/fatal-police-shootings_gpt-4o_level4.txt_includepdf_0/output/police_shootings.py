# Open the data file
data_file = open("fatal-police-shootings-data.csv", 'r')

# Read all lines from the file
data_lines = data_file.readlines()

# Initialize an empty dictionary to store the data
database = {}

# Iterate through each row in the data file, starting from the second row
for row in range(1, len(data_lines)):
    line = data_lines[row]  # Get the current line
    entries = line.split(',')  # Split the line into entries based on commas
    db_entry = {}  # Initialize an empty dictionary for the current entry
    
    # Map the relevant columns to the dictionary
    db_entry["name"] = entries[1]
    db_entry["date"] = entries[2]
    db_entry["armed"] = entries[4]
    db_entry["age"] = entries[5]
    db_entry["gender"] = entries[6]
    db_entry["race"] = entries[7]
    db_entry["state"] = entries[9]
    
    entry_id = int(entries[0])  # Convert the entry ID to an integer
    database[entry_id] = db_entry  # Add the entry to the database dictionary

# Task 3: Write additional code to analyze the data
# 1. Print the name of the subject of the fatal police shooting with ID number 1694
print("Name of the subject with ID 1694:", database[1694]["name"])

# 2. Print the name of all subjects of fatal police shootings in Minnesota
print("Names of subjects in Minnesota:")
for entry_id, entry in database.items():
    if entry["state"] == "MN":
        print(entry["name"])

# 3. Create a new dictionary, race_counts, to count occurrences of each race
race_counts = {}
for entry_id, entry in database.items():
    race = entry["race"]
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# 4. Print the fraction of fatal police shootings with a black subject
black_shootings = race_counts.get('B', 0)
total_shootings = len(database)
fraction_black_shootings = black_shootings / total_shootings
print("Fraction of fatal police shootings with a black subject:", fraction_black_shootings)

# Next part: Analyze unarmed fatal police shootings
# 1. Create a new dictionary called unarmed_selection
unarmed_selection = {entry_id: entry for entry_id, entry in database.items() if entry["armed"] == "unarmed"}

# 2. Create a new dictionary called unarmed_race_counts
unarmed_race_counts = {}
for entry_id, entry in unarmed_selection.items():
    race = entry["race"]
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# 3. Print the fraction of unarmed fatal police shootings with a black subject
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
total_unarmed_shootings = len(unarmed_selection)
fraction_unarmed_black_shootings = unarmed_black_shootings / total_unarmed_shootings
print("Fraction of unarmed fatal police shootings with a black subject:", fraction_unarmed_black_shootings)