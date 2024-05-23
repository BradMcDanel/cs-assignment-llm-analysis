# Open the CSV file for reading
data_file = open("fatal-police-shootings-data.csv", 'r')

# Read all lines from the file
data_lines = data_file.readlines()

# Initialize an empty dictionary to store the data
database = {}

# Iterate over the lines in the file (skipping the first line, which is the header)
for row in range(1, len(data_lines)):
    line = data_lines[row]  # Get the current line
    entries = line.split(',')  # Split the line into entries based on commas
    
    # Create a dictionary entry for the current row
    db_entry = {
        "name": entries[11],
        "date": entries[1],
        "armed": entries[4],
        "age": entries[12],
        "gender": entries[13],
        "race": entries[14],
        "state": entries[9]
    }
    
    # Use the ID from the first column as the key in the database
    entry_id = int(entries[0])
    database[entry_id] = db_entry

# Task 3: Additional code starts here

# Print the name of the subject of the fatal police shooting with ID number 1694
print(f"Name of the subject with ID 1694: {database[1694]['name']}")

# Print the names of all subjects of fatal police shootings in Minnesota
print("Subjects of fatal police shootings in Minnesota:")
for entry_id, entry in database.items():
    if entry['state'] == "MN":
        print(entry['name'])

# Create a new dictionary, race_counts, to count the number of occurrences of each race
race_counts = {}
for entry in database.values():
    race = entry['race']
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Print the fraction of fatal police shootings with a black subject
total_shootings = len(database)
black_shootings = race_counts.get('B', 0)
black_fraction = black_shootings / total_shootings
print(f"Fraction of fatal police shootings with a black subject: {black_fraction}")

# Create a new dictionary, unarmed_selection, for unarmed fatal police shootings
unarmed_selection = {}
for entry_id, entry in database.items():
    if entry['armed'].lower() == "unarmed":
        unarmed_selection[entry_id] = entry

# Create a new dictionary, unarmed_race_counts, to count races among unarmed subjects
unarmed_race_counts = {}
for entry in unarmed_selection.values():
    race = entry['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Print the fraction of unarmed fatal police shootings with a black subject
total_unarmed_shootings = len(unarmed_selection)
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
unarmed_black_fraction = unarmed_black_shootings / total_unarmed_shootings
print(f"Fraction of unarmed fatal police shootings with a black subject: {unarmed_black_fraction}")