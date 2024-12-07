# Given that the dictionary `database` is already constructed:

# Task 3.1: Print the name of the subject with ID number 1694
print("Name of subject with ID 1694:", database['1694']['name'])

# Task 3.2: Print the names of all subjects of fatal police shootings in Minnesota
print("Subjects of fatal police shootings in Minnesota:")
for record in database.values():
    if record['state'] == 'MN':
        print(record['name'])

# Task 3.3: Create a dictionary for race counts
race_counts = {}
for record in database.values():
    race = record['race']
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Task 3.4: Print the fraction of fatal police shootings with a black subject
black_shootings = race_counts.get('B', 0)
total_shootings = len(database)
black_fraction = black_shootings / total_shootings
print("Fraction of fatal police shootings with a black subject:", black_fraction)

# Task 3.5: Create a dictionary for unarmed selection
unarmed_selection = {key: value for key, value in database.items() if value['armed'] == 'unarmed'}

# Task 3.6: Create a dictionary for unarmed race counts
unarmed_race_counts = {}
for record in unarmed_selection.values():
    race = record['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Task 3.7: Print the fraction of unarmed fatal police shootings with a black subject
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
total_unarmed_shootings = len(unarmed_selection)
unarmed_black_fraction = unarmed_black_shootings / total_unarmed_shootings
print("Fraction of unarmed fatal police shootings with a black subject:", unarmed_black_fraction)