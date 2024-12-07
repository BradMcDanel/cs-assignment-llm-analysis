# Open the CSV file containing the data on fatal police shootings
data_file = open("fatal-police-shootings-data.csv", 'r')

# Read all lines from the CSV file
data_lines = data_file.readlines()

# Initialize an empty dictionary to store the data
database = {}

# Start iterating from the second line (index 1) to skip the header
for row in range(1, len(data_lines)):
    # Read a line from the CSV file
    line = data_lines[row]
    
    # Split the line by commas to separate values
    entries = line.split(',')
    
    # Create a dictionary entry for each line with relevant details
    db_entry = {}
    db_entry["name"] = entries[11]
    db_entry["date"] = entries[1]
    db_entry["armed"] = entries[4]
    db_entry["age"] = entries[12]
    db_entry["gender"] = entries[13]
    db_entry["race"] = entries[14]
    db_entry["state"] = entries[8]
    
    # Use the 'id' from the CSV as the key for the dictionary
    entry_id = int(entries[0])
    database[entry_id] = db_entry

# Task 3: Additional code

# Print the name of the subject with ID 1694
print("Name of the subject with ID 1694:", database[1694]['name'])

# Print the names of all subjects of fatal police shootings in Minnesota
print("Fatal police shootings in Minnesota:")
for entry in database.values():
    if entry['state'] == 'MN':
        print(entry['name'])

# Create a dictionary to count races
race_counts = {}
for entry in database.values():
    race = entry['race']
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Calculate and print the fraction of fatal police shootings with a black subject
black_shootings = race_counts.get('B', 0)
total_shootings = len(database)
fraction_black_shootings = black_shootings / total_shootings
print("Fraction of fatal police shootings with a black subject:", fraction_black_shootings)

# Create an unarmed selection dictionary
unarmed_selection = {}
for key, entry in database.items():
    if entry['armed'].lower() == 'unarmed':
        unarmed_selection[key] = entry

# Create a dictionary to count races among unarmed subjects
unarmed_race_counts = {}
for entry in unarmed_selection.values():
    race = entry['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Calculate and print the fraction of unarmed fatal police shootings with a black subject
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
total_unarmed_shootings = len(unarmed_selection)
fraction_unarmed_black_shootings = unarmed_black_shootings / total_unarmed_shootings
print("Fraction of unarmed fatal police shootings with a black subject:", fraction_unarmed_black_shootings)