import csv

# Task 2: Reading the data into a dictionary
def read_data():
    database = {}
    with open('fatal-police-shootings-data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            entry_id = int(row['id'])
            database[entry_id] = {
                'name': row['name'],
                'date': row['date'],
                'armed': row['armed_with'],
                'age': row['age'],
                'gender': row['gender'],
                'race': row['race'],
                'state': row['state']
            }
    return database

# Task 3: Using the database
def analyze_data(database):
    # Print the name of the subject with ID number 1694
    print(f"Subject with ID 1694: {database[1694]['name']}")

    # Print names of all subjects in Minnesota
    print("\nSubjects in Minnesota:")
    for entry in database.values():
        if entry['state'] == 'MN':
            print(entry['name'])

    # Count occurrences of each race
    race_counts = {}
    for entry in database.values():
        race = entry['race']
        race_counts[race] = race_counts.get(race, 0) + 1

    # Calculate and print the fraction of fatal police shootings with a black subject
    total_shootings = len(database)
    black_shootings = race_counts.get('B', 0)
    black_fraction = black_shootings / total_shootings
    print(f"\nFraction of fatal police shootings with a black subject: {black_fraction:.3f}")

    # Analyze unarmed shootings
    unarmed_selection = {id: entry for id, entry in database.items() if entry['armed'] == 'unarmed'}
    unarmed_race_counts = {}
    for entry in unarmed_selection.values():
        race = entry['race']
        unarmed_race_counts[race] = unarmed_race_counts.get(race, 0) + 1

    # Calculate and print the fraction of unarmed fatal police shootings with a black subject
    total_unarmed_shootings = len(unarmed_selection)
    unarmed_black_shootings = unarmed_race_counts.get('B', 0)
    unarmed_black_fraction = unarmed_black_shootings / total_unarmed_shootings
    print(f"Fraction of unarmed fatal police shootings with a black subject: {unarmed_black_fraction:.3f}")

if __name__ == "__main__":
    database = read_data()
    analyze_data(database)