# Print the name of the subject of the fatal police shooting with ID number 1694
print("Name of subject with ID 1694:", database['1694']['name'])

# Print the names of all subjects of fatal police shootings in Minnesota
print("Subjects of fatal police shootings in Minnesota:")
for record in database.values():
    if record['state'] == 'MN':
        print(record['name'])

# Create a dictionary to count occurrences of each race
race_counts = {}
for record in database.values():
    race = record['race']
    if race not in race_counts:
        race_counts[race] = 0
    race_counts[race] += 1

# Print the fraction of fatal police shootings with a black subject
black_fraction = race_counts.get('B', 0) / len(database)
print("Fraction of fatal police shootings with a black subject:", black_fraction)

# Task 3 Questions
# Question 1: The proportion of black subjects in fatal police shootings is much higher than their representation in the general U.S. population, indicating a disparity.

# Create a dictionary for unarmed selections
unarmed_selection = {key: value for key, value in database.items() if value['armed'] == 'unarmed'}

# Create a dictionary to count occurrences of each race among unarmed subjects
unarmed_race_counts = {}
for record in unarmed_selection.values():
    race = record['race']
    if race not in unarmed_race_counts:
        unarmed_race_counts[race] = 0
    unarmed_race_counts[race] += 1

# Print the fraction of unarmed fatal police shootings with a black subject
unarmed_black_fraction = unarmed_race_counts.get('B', 0) / len(unarmed_selection)
print("Fraction of unarmed fatal police shootings with a black subject:", unarmed_black_fraction)

# Task 3 Questions
# Question 2: The proportion of unarmed black subjects in fatal police shootings is also disproportionately high compared to their representation in the U.S. population and similar to the general proportion of black subjects in all police shootings.