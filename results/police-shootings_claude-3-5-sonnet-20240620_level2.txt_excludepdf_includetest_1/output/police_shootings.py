# Print name of subject with ID 1694
print(f"Subject with ID 1694: {database['1694'][0]}")

# Print names of subjects in Minnesota
print("Subjects in Minnesota:")
for id, data in database.items():
    if data[2] == 'MN':
        print(data[0])

# Count occurrences of each race
race_counts = {}
for data in database.values():
    race = data[3]
    race_counts[race] = race_counts.get(race, 0) + 1

# Calculate fraction of shootings with black subjects
total_shootings = len(database)
black_shootings = race_counts.get('B', 0)
black_fraction = black_shootings / total_shootings

print(f"Fraction of shootings with black subjects: {black_fraction:.2f}")

# ... More code for unarmed shootings analysis ...