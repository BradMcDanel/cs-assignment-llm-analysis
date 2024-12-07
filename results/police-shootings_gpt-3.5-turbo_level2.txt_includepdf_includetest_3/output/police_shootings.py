# Continue writing code for Task 3

# Create a new dictionary for unarmed subjects
unarmed_selection = {}
for entry_id, details in database.items():
    if details["armed"] == "unarmed":
        unarmed_selection[entry_id] = details

# Create a new dictionary to count occurrences of each race among unarmed subjects
unarmed_race_counts = {}
for details in unarmed_selection.values():
    race = details["race"]
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Print the fraction of unarmed fatal police shootings with a black subject
total_unarmed_shootings = len(unarmed_selection)
black_unarmed_shootings = unarmed_race_counts.get("B", 0)
fraction_black_unarmed_shootings = black_unarmed_shootings / total_unarmed_shootings
print(fraction_black_unarmed_shootings)