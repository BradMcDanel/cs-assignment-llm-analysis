import csv

# Open the CSV file containing the data on fatal police shootings.
with open('fatal-police-shootings-data.csv', mode='r') as file:
    # Create a CSV reader object to iterate over lines in the CSV file.
    csv_reader = csv.reader(file)
    
    # Skip the header row to access the data directly.
    next(csv_reader)

    # Initialize an empty dictionary to store the data.
    database = {}

    # Iterate over each row in the CSV file.
    for row in csv_reader:
        # Use the 'id' as the key for the dictionary since it is unique for each record.
        key = int(row[0])
        # Store the relevant row data as a dictionary for each 'id'.
        database[key] = {
            'name': row[1],
            'date': row[2],
            'manner_of_death': row[3],
            'armed': row[4],
            'age': row[5],
            'gender': row[6],
            'race': row[7],
            'city': row[8],
            'state': row[9],
            'signs_of_mental_illness': row[10],
            'threat_level': row[11],
            'flee': row[12],
            'body_camera': row[13],
            'is_geocoding_exact': row[14]
        }

# Task 3: Using the database
# Print the name of the subject of the fatal police shooting with ID number 1694.
print("Name of subject with ID 1694:", database[1694]['name'])

# Print the name of all subjects of fatal police shootings in Minnesota.
print("Names of subjects in Minnesota:")
for key, value in database.items():
    if value['state'] == 'MN':
        print(value['name'])

# Create a new dictionary called race_counts.
race_counts = {}
for value in database.values():
    race = value['race']
    race_counts[race] = race_counts.get(race, 0) + 1

# Print the fraction of fatal police shootings with a black subject.
black_shootings = race_counts.get('B', 0)
total_shootings = len(database)
print("Fraction of fatal police shootings with a black subject:", black_shootings / total_shootings)

# Filter for unarmed subjects.
unarmed_selection = {k: v for k, v in database.items() if v['armed'] == 'unarmed'}

# Create a new dictionary called unarmed_race_counts.
unarmed_race_counts = {}
for value in unarmed_selection.values():
    race = value['race']
    unarmed_race_counts[race] = unarmed_race_counts.get(race, 0) + 1

# Print the fraction of unarmed fatal police shootings with a black subject.
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
total_unarmed_shootings = len(unarmed_selection)
print("Fraction of unarmed fatal police shootings with a black subject:", unarmed_black_shootings / total_unarmed_shootings)