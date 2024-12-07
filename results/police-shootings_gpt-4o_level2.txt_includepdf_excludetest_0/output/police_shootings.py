# Open the .csv file containing the data
data_file = open("fatal-police-shootings-data.csv", 'r')

# Read all lines from the data file
data_lines = data_file.readlines()

# Initialize an empty dictionary to store the data
database = {}

# Loop through each row in the data file, starting from the second line (to skip the header)
for row in range(1, len(data_lines)):
    line = data_lines[row]  # Get the current line
    entries = line.split(',')  # Split the line by commas to separate the fields
    
    # Create a dictionary entry for this row
    db_entry = {}
    db_entry["name"] = entries[1]  # Store the name of the subject
    db_entry["date"] = entries[2]  # Store the date of the incident
    db_entry["armed"] = entries[4]  # Store whether the subject was armed
    db_entry["age"] = entries[5]  # Store the age of the subject
    db_entry["gender"] = entries[6]  # Store the gender of the subject
    db_entry["race"] = entries[7]  # Store the race of the subject
    db_entry["state"] = entries[9]  # Store the state where the incident occurred
    
    # Use the id as the key in the database
    entry_id = int(entries[0])
    database[entry_id] = db_entry

# Task 3: Continuing with the provided code

# Print the name of the subject with ID number 1694
subject_id = 1694
if subject_id in database:
    print(f"Name of subject with ID {subject_id}: {database[subject_id]['name']}")

# Print the names of all subjects of fatal police shootings in Minnesota
print("Subjects of fatal police shootings in Minnesota:")
for entry_id, details in database.items():
    if details['state'] == 'MN':
        print(details['name'])

# Construct a dictionary to count the number of occurrences of each race
race_counts = {}
for entry_id, details in database.items():
    race = details['race']
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Print the fraction of fatal police shootings with a black subject
total_shootings = len(database)
black_shootings = race_counts.get('B', 0)
print(f"Fraction of fatal police shootings with a black subject: {black_shootings / total_shootings}")

# Restrict to unarmed shootings
unarmed_selection = {}
for entry_id, details in database.items():
    if details['armed'].lower() == 'unarmed':
        unarmed_selection[entry_id] = details

# Construct race counts for unarmed shootings
unarmed_race_counts = {}
for entry_id, details in unarmed_selection.items():
    race = details['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Print the fraction of unarmed fatal police shootings with a black subject
total_unarmed_shootings = len(unarmed_selection)
black_unarmed_shootings = unarmed_race_counts.get('B', 0)
print(f"Fraction of unarmed fatal police shootings with a black subject: {black_unarmed_shootings / total_unarmed_shootings}")