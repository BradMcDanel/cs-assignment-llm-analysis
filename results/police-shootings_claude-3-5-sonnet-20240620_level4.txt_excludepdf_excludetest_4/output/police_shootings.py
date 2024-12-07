import csv

# Read the data from the CSV file and create a dictionary
def read_data(filename):
    database = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id = row['id']
            database[id] = {
                'name': row['name'],
                'date': row['date'],
                'manner_of_death': row['manner_of_death'],
                'armed': row['armed'],
                'age': row['age'],
                'gender': row['gender'],
                'race': row['race'],
                'city': row['city'],
                'state': row['state'],
                'signs_of_mental_illness': row['signs_of_mental_illness'],
                'threat_level': row['threat_level'],
                'flee': row['flee'],
                'body_camera': row['body_camera']
            }
    return database

# Main execution
if __name__ == "__main__":
    database = read_data('fatal-police-shootings-data.csv')

    # Print the name of the subject with ID number 1694
    print(f"Subject with ID 1694: {database['1694']['name']}")

    # Print names of all subjects in Minnesota
    print("\nSubjects in Minnesota:")
    for id, data in database.items():
        if data['state'] == 'MN':
            print(data['name'])

    # Create race_counts dictionary
    race_counts = {}
    for data in database.values():
        race = data['race']
        race_counts[race] = race_counts.get(race, 0) + 1

    # Print fraction of fatal police shootings with a black subject
    total_shootings = len(database)
    black_shootings = race_counts.get('B', 0)
    black_fraction = black_shootings / total_shootings
    print(f"\nFraction of fatal police shootings with a black subject: {black_fraction:.4f}")

    # Create unarmed_selection dictionary
    unarmed_selection = {id: data for id, data in database.items() if data['armed'] == 'unarmed'}

    # Create unarmed_race_counts dictionary
    unarmed_race_counts = {}
    for data in unarmed_selection.values():
        race = data['race']
        unarmed_race_counts[race] = unarmed_race_counts.get(race, 0) + 1

    # Print fraction of unarmed fatal police shootings with a black subject
    total_unarmed_shootings = len(unarmed_selection)
    black_unarmed_shootings = unarmed_race_counts.get('B', 0)
    black_unarmed_fraction = black_unarmed_shootings / total_unarmed_shootings
    print(f"Fraction of unarmed fatal police shootings with a black subject: {black_unarmed_fraction:.4f}")