import police_shootings

# Print the name of the subject of the fatal police shooting with ID number 1694
if 1694 in police_shootings.database:
    print(police_shootings.database[1694]["name"])

# Print the names of all subjects of fatal police shootings in Minnesota
for key, value in police_shootings.database.items():
    if value["state"] == "MN":
        print(value["name"])

# Create a new dictionary race counts to count the occurrences of each race
race_counts = {}
for key, value in police_shootings.database.items():
    race = value["race"]
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

# Print the fraction of fatal police shootings with a black subject
total_fatal_shootings = len(police_shootings.database)
black_fatal_shootings = race_counts.get("B", 0)
fraction_black_fatal_shootings = black_fatal_shootings / total_fatal_shootings
print(fraction_black_fatal_shootings)