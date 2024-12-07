# ... (previous code remains the same)

# Print the name of the subject with ID number 1694
with open('fatal-police-shootings-data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        if row['id'] == '1694':
            print(f"The name of the subject with ID 1694 is: {row['name']}")
            break

# Print names of all subjects in Minnesota
print("\nNames of subjects in Minnesota:")
with open('fatal-police-shootings-data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        if row['state'] == 'MN':
            print(row['name'])

# Create race_counts dictionary
race_counts = {}
for incident in database.values():
    race = incident['race']
    race_counts[race] = race_counts.get(race, 0) + 1

# Print fraction of fatal police shootings with a black subject
total_shootings = sum(race_counts.values())
black_shootings = race_counts.get('B', 0)
black_fraction = black_shootings / total_shootings
print(f"\nFraction of fatal police shootings with a black subject: {black_fraction:.4f}")

# Create unarmed_selection dictionary
unarmed_selection = {k: v for k, v in database.items() if v['armed'] == 'unarmed'}

# Create unarmed_race_counts dictionary
unarmed_race_counts = {}
for incident in unarmed_selection.values():
    race = incident['race']
    unarmed_race_counts[race] = unarmed_race_counts.get(race, 0) + 1

# Print fraction of unarmed fatal police shootings with a black subject
total_unarmed_shootings = sum(unarmed_race_counts.values())
unarmed_black_shootings = unarmed_race_counts.get('B', 0)
unarmed_black_fraction = unarmed_black_shootings / total_unarmed_shootings
print(f"\nFraction of unarmed fatal police shootings with a black subject: {unarmed_black_fraction:.4f}")