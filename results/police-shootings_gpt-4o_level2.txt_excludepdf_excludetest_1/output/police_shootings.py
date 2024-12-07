# Create a dictionary for unarmed fatal police shootings
unarmed_selection = {}
for key, incident in database.items():
    if incident['armed'] == 'unarmed':
        unarmed_selection[key] = incident

# Create a dictionary to count occurrences of each race among unarmed subjects
unarmed_race_counts = {}
for incident in unarmed_selection.values():
    race = incident['race']
    if race in unarmed_race_counts:
        unarmed_race_counts[race] += 1
    else:
        unarmed_race_counts[race] = 1

# Print the fraction of unarmed fatal police shootings with a black subject
unarmed_black_count = unarmed_race_counts.get('B', 0)
total_unarmed_count = len(unarmed_selection)
unarmed_black_fraction = unarmed_black_count / total_unarmed_count
print("Fraction of unarmed fatal police shootings with a black subject:", unarmed_black_fraction)