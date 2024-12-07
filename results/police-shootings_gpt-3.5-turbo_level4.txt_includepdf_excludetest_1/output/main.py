import datetime

# Print the name of the subject of the fatal police shooting with ID number 1694
subject_1694 = database[1694]["name"]
print(subject_1694)

# Print the name of all subjects of fatal police shootings in Minnesota
for key, value in database.items():
    if value["state"] == "MN":
        print(value["name"])

# Create a new dictionary race counts
race_counts = {}
for key, value in database.items():
    race = value["race"]
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Print the fraction of fatal police shootings with a black subject
total_shootings = len(database)
black_shootings = race_counts.get("B", 0)
fraction_black_shootings = black_shootings / total_shootings
print(fraction_black_shootings)

# Create a new dictionary unarmed selection
unarmed_selection = {}
for key, value in database.items():
    if value["armed"] == "unarmed":
        unarmed_selection[key] = value

# Create a new dictionary unarmed race counts
unarmed_race_counts = {}
for key, value in unarmed_selection.items():
    race = value["race"]
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Print the fraction of unarmed fatal police shootings with a black subject
total_unarmed_shootings = len(unarmed_selection)
black_unarmed_shootings = unarmed_race_counts.get("B", 0)
fraction_black_unarmed_shootings = black_unarmed_shootings / total_unarmed_shootings
print(fraction_black_unarmed_shootings)