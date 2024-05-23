import csv

# Task 2: Reading the data into a dictionary
# The provided code reads the .csv file and creates a dictionary named `database`.

def read_data(filename):
    """
    Reads CSV data from the specified file and returns a dictionary where the keys are the 'id' of each
    shooting and the values are dictionaries of the other data fields associated with that shooting.
    """
    database = {}
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Use the 'id' field as the key
            key = int(row['id'])
            # Store the rest of the data as a dictionary
            database[key] = row
    return database

# Read the data from the CSV file
database = read_data('fatal-police-shootings-data.csv')

# Task 3: Using the database
# Print the name of the subject of the fatal police shooting with ID number 1694
print(f"Subject with ID 1694: {database[1694]['name']}")

# Print the names of all subjects of fatal police shootings in Minnesota
print("Subjects of fatal police shootings in Minnesota:")
for key, value in database.items():
    if value['state'] == 'MN':
        print(value['name'])

# Create a dictionary to count the occurrences of each race in fatal police shootings
race_counts = {}
for key, value in database.items():
    race = value['race']
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Print the fraction of fatal police shootings with a black subject
total_shootings = len(database)
black_shootings = race_counts.get('B', 0)
print(f"Fraction of fatal police shootings with a black subject: {black_shootings / total_shootings:.2f}")

# Create a dictionary for unarmed fatal police shootings
unarmed_selection = {}
for key, value in database.items():
    if value['armed'] == 'unarmed':
        unarmed_selection[key] = value

# Create a dictionary to count the occurrences of each race in unarmed fatal police shootings
unarmed_race_counts = {}
for key, value in unarmed_selection.items():
    race = value['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Print the fraction of unarmed fatal police shootings with a black subject
total_unarmed_shootings = len(unarmed_selection)
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
print(f"Fraction of unarmed fatal police shootings with a black subject: {unarmed_black_shootings / total_unarmed_shootings:.2f}")