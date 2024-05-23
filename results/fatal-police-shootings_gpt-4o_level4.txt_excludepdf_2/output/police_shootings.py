import csv

# Initialize an empty dictionary to store the data
database = {}

# Open the CSV file containing the data
with open('fatal-police-shootings-data.csv') as csvfile:
    # Create a CSV reader object to read the file
    reader = csv.DictReader(csvfile)
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Use the "id" column as the key for the dictionary
        key = row['id']
        
        # Store the row data in the dictionary under the corresponding key
        database[key] = row

# Task 3: Write additional code to analyze the data
# 1. Print the name of the subject of the fatal police shooting with ID number 1694

subject_1694 = database['1694']['name']
print(f"Name of subject with ID 1694: {subject_1694}")

# 2. Print the name of all subjects of fatal police shootings in Minnesota

print("Subjects of fatal police shootings in Minnesota:")
for entry in database.values():
    if entry['state'] == 'MN':
        print(entry['name'])

# 3. Create a dictionary to count the number of occurrences of each race

race_counts = {}
for entry in database.values():
    race = entry['race']
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Print the race counts dictionary
print("Race counts:", race_counts)

# 4. Print the fraction of fatal police shootings with a black subject

black_count = race_counts.get('B', 0)
total_shootings = len(database)
fraction_black = black_count / total_shootings
print(f"Fraction of fatal police shootings with a black subject: {fraction_black}")

# Additional tasks for unarmed subjects
# 1. Create a new dictionary for unarmed subjects

unarmed_selection = {}
for key, entry in database.items():
    if entry['armed'] == 'unarmed':
        unarmed_selection[key] = entry

# 2. Create a dictionary to count the number of occurrences of each race among unarmed subjects

unarmed_race_counts = {}
for entry in unarmed_selection.values():
    race = entry['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Print the unarmed race counts dictionary
print("Unarmed race counts:", unarmed_race_counts)

# 3. Print the fraction of unarmed fatal police shootings with a black subject

unarmed_black_count = unarmed_race_counts.get('B', 0)
total_unarmed_shootings = len(unarmed_selection)
fraction_unarmed_black = unarmed_black_count / total_unarmed_shootings
print(f"Fraction of unarmed fatal police shootings with a black subject: {fraction_unarmed_black}")