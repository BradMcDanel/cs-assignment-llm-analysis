# Open the CSV file containing the data
data_file = open("fatal-police-shootings-data.csv", 'r')

# Read all lines from the file
data_lines = data_file.readlines()

# Initialize an empty dictionary to store the data
database = {}

# Loop through each line in the file starting from the second line (skip header)
for row in range(1, len(data_lines)):
    line = data_lines[row]
    # Split the line by commas to separate the columns
    entries = line.split(',')
    # Create a dictionary for each entry
    db_entry = {}
    db_entry["name"] = entries[12]  # Store the name
    db_entry["date"] = entries[1]   # Store the date
    db_entry["armed"] = entries[4]  # Store whether the person was armed
    db_entry["age"] = entries[13]   # Store the age
    db_entry["gender"] = entries[14]  # Store the gender
    db_entry["race"] = entries[15]  # Store the race
    db_entry["state"] = entries[8]  # Store the state
    entry_id = int(entries[0])  # Use the ID as the key in the dictionary
    database[entry_id] = db_entry   # Add the entry to the database with ID as the key

# Task 3: Additional Code
# Print the name of the subject with ID number 1694
print("Name of subject with ID 1694:", database[1694]["name"])

# Print the names of all subjects of fatal police shootings in Minnesota
print("Subjects of fatal police shootings in Minnesota:")
for entry_id, details in database.items():
    if details["state"] == "MN":  # Check if the state is Minnesota
        print(details["name"])

# Create a dictionary to count the occurrences of each race
race_counts = {}
for entry_id, details in database.items():
    race = details["race"]
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Print the race counts
print("Race counts:", race_counts)

# Calculate and print the fraction of fatal police shootings with a black subject
total_shootings = len(database)
black_shootings = race_counts.get("B", 0)
fraction_black_shootings = black_shootings / total_shootings
print("Fraction of fatal police shootings with a black subject:", fraction_black_shootings)

# Create a dictionary for unarmed fatal police shootings
unarmed_selection = {}
for entry_id, details in database.items():
    if details["armed"] == "unarmed":  # Check if the person was unarmed
        unarmed_selection[entry_id] = details

# Create a dictionary to count the occurrences of each race in unarmed shootings
unarmed_race_counts = {}
for entry_id, details in unarmed_selection.items():
    race = details["race"]
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Print the unarmed race counts
print("Unarmed race counts:", unarmed_race_counts)

# Calculate and print the fraction of unarmed fatal police shootings with a black subject
total_unarmed_shootings = len(unarmed_selection)
black_unarmed_shootings = unarmed_race_counts.get("B", 0)
fraction_black_unarmed_shootings = black_unarmed_shootings / total_unarmed_shootings
print("Fraction of unarmed fatal police shootings with a black subject:", fraction_black_unarmed_shootings)

# Close the data file
data_file.close()