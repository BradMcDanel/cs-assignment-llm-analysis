import csv

# Step 1: Read data from CSV and store it in a dictionary
database = {}

with open('fatal-police-shootings-data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Using 'id' as the key for our main database dictionary
        database[row['id']] = row

# Task 3: Analyze the data

# 1. Print the name of the subject of the fatal police shooting with ID number 1694
if '1694' in database:
    print("Name of the subject with ID 1694:", database['1694']['name'])

# 2. Print the names of all subjects of fatal police shootings in Minnesota
print("Subjects of fatal police shootings in Minnesota:")
for record in database.values():
    if record['state'] == 'MN':
        print(record['name'])

# 3. Create a race counts dictionary
race_counts = {}
for record in database.values():
    race = record['race']
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# 4. Print the fraction of fatal police shootings with a black subject
black_shootings = race_counts.get('B', 0)
total_shootings = len(database)
fraction_black_shootings = black_shootings / total_shootings
print("Fraction of fatal police shootings with a black subject:", fraction_black_shootings)

# Further analysis on unarmed subjects
unarmed_selection = {key: value for key, value in database.items() if value['armed'] == 'unarmed'}

unarmed_race_counts = {}
for record in unarmed_selection.values():
    race = record['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# 5. Print the fraction of unarmed fatal police shootings with a black subject
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
total_unarmed_shootings = len(unarmed_selection)
fraction_unarmed_black_shootings = unarmed_black_shootings / total_unarmed_shootings
print("Fraction of unarmed fatal police shootings with a black subject:", fraction_unarmed_black_shootings)