# Open the CSV file containing the police shooting data
data_file = open("fatal-police-shootings-data.csv", 'r')

# Read all lines from the CSV file
data_lines = data_file.readlines()

# Initialize an empty dictionary to store the data
database = {}

# Iterate over each line in the CSV file, starting from the second line
# (skip the header line)
for row in range(1, len(data_lines)):
    line = data_lines[row]
    
    # Split the line into individual data entries based on commas
    entries = line.split(',')
    
    # Create a dictionary for each data entry with relevant fields
    db_entry = {}
    db_entry["name"] = entries[11]
    db_entry["date"] = entries[1]
    db_entry["armed"] = entries[4]
    db_entry["age"] = entries[12]
    db_entry["gender"] = entries[13]
    db_entry["race"] = entries[14]
    db_entry["state"] = entries[8]
    
    # Use the ID from the entry as the key for the database
    entry_id = int(entries[0])
    database[entry_id] = db_entry

# Task 3: Using the Database

# Print the name of the subject with ID 1694
subject_1694 = database.get(1694)
if subject_1694:
    print("Subject with ID 1694:", subject_1694["name"])

# Print the names of all subjects of fatal police shootings in Minnesota
print("Subjects of fatal police shootings in Minnesota:")
for entry_id, details in database.items():
    if details["state"] == "MN":
        print(details["name"])

# Create a dictionary to count races
race_counts = {}
for details in database.values():
    race = details["race"]
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Calculate and print the fraction of fatal police shootings with a black subject
total_shootings = len(database)
black_shootings = race_counts.get('B', 0)
black_fraction = black_shootings / total_shootings if total_shootings > 0 else 0
print("Fraction of fatal police shootings with a black subject:", black_fraction)

# Create a dictionary for unarmed selection
unarmed_selection = {entry_id: details for entry_id, details in database.items() if details["armed"] == "unarmed"}

# Create a dictionary to count races among unarmed subjects
unarmed_race_counts = {}
for details in unarmed_selection.values():
    race = details["race"]
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Calculate and print the fraction of unarmed fatal police shootings with a black subject
total_unarmed_shootings = len(unarmed_selection)
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
unarmed_black_fraction = unarmed_black_shootings / total_unarmed_shootings if total_unarmed_shootings > 0 else 0
print("Fraction of unarmed fatal police shootings with a black subject:", unarmed_black_fraction)