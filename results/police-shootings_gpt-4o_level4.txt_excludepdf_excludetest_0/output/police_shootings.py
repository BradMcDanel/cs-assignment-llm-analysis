import csv

# Read the CSV file and store its contents in a dictionary
with open('fatal-police-shootings-data.csv', newline='', encoding='utf-8') as csvfile:
    datareader = csv.DictReader(csvfile)
    database = {row['id']: row for row in datareader}

# Task 3: Implement the required data analysis tasks

# 1. Print the name of the subject with ID 1694
subject_id = '1694'
if subject_id in database:
    print(f"Name of subject with ID {subject_id}: {database[subject_id]['name']}")

# 2. Print the names of all subjects in Minnesota
print("Subjects in Minnesota:")
for entry in database.values():
    if entry['state'] == 'MN':
        print(entry['name'])

# 3. Create a race counts dictionary
race_counts = {}
for entry in database.values():
    race = entry['race']
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# 4. Print the fraction of fatal police shootings with a black subject
black_shootings = race_counts.get('B', 0)
total_shootings = len(database)
fraction_black = black_shootings / total_shootings if total_shootings > 0 else 0
print(f"Fraction of fatal police shootings with a black subject: {fraction_black:.4f}")

# Additional Task: Unarmed selection
unarmed_selection = {key: value for key, value in database.items() if value['armed'] == 'unarmed'}

# Unarmed race counts
unarmed_race_counts = {}
for entry in unarmed_selection.values():
    race = entry['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Print the fraction of unarmed fatal police shootings with a black subject
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
total_unarmed_shootings = len(unarmed_selection)
fraction_unarmed_black = unarmed_black_shootings / total_unarmed_shootings if total_unarmed_shootings > 0 else 0
print(f"Fraction of unarmed fatal police shootings with a black subject: {fraction_unarmed_black:.4f}")