# Open the data file and read the lines
data_file = open("fatal-police-shootings-data.csv", 'r')
data_lines = data_file.readlines()

# Initialize a dictionary to store the data
database = {}

# Populate the database dictionary with data from the CSV file
for row in range(1, len(data_lines)):
    line = data_lines[row]
    entries = line.strip().split(',')
    db_entry = {}
    db_entry["name"] = entries[11]
    db_entry["date"] = entries[1]
    db_entry["armed"] = entries[4]
    db_entry["age"] = entries[12]
    db_entry["gender"] = entries[13]
    db_entry["race"] = entries[14]
    db_entry["state"] = entries[7]
    entry_id = int(entries[0])
    database[entry_id] = db_entry

# Task 3: Print the name of the subject with ID number 1694
subject_id_1694 = database.get(1694, {}).get("name", "Unknown")
print(f"Name of subject with ID 1694: {subject_id_1694}")

# Task 3: Print the names of all subjects of fatal police shootings in Minnesota
print("Subjects of fatal police shootings in Minnesota:")
for entry in database.values():
    if entry["state"] == "MN":
        print(entry["name"])

# Task 3: Create a dictionary to count occurrences of each race
race_counts = {}
for entry in database.values():
    race = entry["race"]
    if race:
        if race in race_counts:
            race_counts[race] += 1
        else:
            race_counts[race] = 1

# Calculate and print the fraction of fatal police shootings with a black subject
black_shootings = race_counts.get("B", 0)
total_shootings = len(database)
black_fraction = black_shootings / total_shootings
print(f"Fraction of fatal police shootings with a black subject: {black_fraction:.3f}")

# Task 3: Create a dictionary for unarmed subjects
unarmed_selection = {id: entry for id, entry in database.items() if entry["armed"] == "unarmed"}

# Task 3: Create a dictionary to count occurrences of each race among unarmed subjects
unarmed_race_counts = {}
for entry in unarmed_selection.values():
    race = entry["race"]
    if race:
        if race in unarmed_race_counts:
            unarmed_race_counts[race] += 1
        else:
            unarmed_race_counts[race] = 1

# Calculate and print the fraction of unarmed fatal police shootings with a black subject
unarmed_black_shootings = unarmed_race_counts.get("B", 0)
total_unarmed_shootings = len(unarmed_selection)
unarmed_black_fraction = unarmed_black_shootings / total_unarmed_shootings
print(f"Fraction of unarmed fatal police shootings with a black subject: {unarmed_black_fraction:.3f}")