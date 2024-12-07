import csv

# Open the CSV file and read its contents
with open('fatal-police-shootings-data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    
    # Initialize an empty dictionary to store the data
    database = {}
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Use the 'id' as the key for the dictionary
        key = row['id']
        
        # Store the entire row (a dictionary) as the value
        database[key] = row

# Task 3: Using the database
# Print the name of the subject of the fatal police shooting with ID number 1694
subject_id_1694 = database['1694']['name']
print(f"The subject of the fatal police shooting with ID 1694 is: {subject_id_1694}")

# Print the name of all subjects of fatal police shootings in Minnesota
print("Subjects of fatal police shootings in Minnesota:")
for entry in database.values():
    if entry['state'] == 'MN':
        print(entry['name'])

# Create a new dictionary, race_counts, to count the number of occurrences of each race
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
print(f"Fraction of fatal police shootings with a black subject: {fraction_black_shootings:.4f}")

# Create a new dictionary, unarmed_selection, for unarmed shootings
unarmed_selection = {key: value for key, value in database.items() if value['armed'] == 'unarmed'}

# Create a new dictionary, unarmed_race_counts, to count the races in unarmed shootings
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
print(f"Fraction of unarmed fatal police shootings with a black subject: {fraction_unarmed_black_shootings:.4f}")