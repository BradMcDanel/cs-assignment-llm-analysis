import csv

# Reading the data from the CSV file
def read_data(filename):
    """Reads data from the CSV file and returns it as a list of dictionaries."""
    with open(filename, newline='', encoding='utf-8') as csvfile:
        data_reader = csv.DictReader(csvfile)
        data = []
        for row in data_reader:
            data.append(row)
        return data

# Organizing data into a dictionary
def create_database(data):
    """Creates a dictionary where the keys are 'id' and values are dictionaries of other data."""
    database = {}
    for entry in data:
        # Use 'id' as the key for the database
        key = entry['id']
        database[key] = {
            'name': entry['name'],
            'date': entry['date'],
            'manner_of_death': entry['manner_of_death'],
            'armed': entry['armed'],
            'age': entry['age'],
            'gender': entry['gender'],
            'race': entry['race'],
            'city': entry['city'],
            'state': entry['state'],
            'signs_of_mental_illness': entry['signs_of_mental_illness'] == 'True',
            'threat_level': entry['threat_level'],
            'flee': entry['flee'],
            'body_camera': entry['body_camera'] == 'True'
        }
    return database

def main():
    # Reading and organizing the data
    data = read_data('fatal-police-shootings-data.csv')
    database = create_database(data)

    # Task 3: Analysis
    # Print the name of the subject with ID 1694
    print("Subject with ID 1694:", database['1694']['name'])

    # Print all subjects from Minnesota
    print("Subjects from Minnesota:")
    for entry in database.values():
        if entry['state'] == 'MN':
            print(entry['name'])

    # Count occurrences of each race
    race_counts = {}
    for entry in database.values():
        race = entry['race']
        if race not in race_counts:
            race_counts[race] = 0
        race_counts[race] += 1

    # Print fraction of shootings with a Black subject
    black_fraction = race_counts.get('B', 0) / len(database)
    print("Fraction of shootings with a Black subject:", black_fraction)

    # Restrict to unarmed shootings
    unarmed_selection = {k: v for k, v in database.items() if v['armed'] == 'unarmed'}

    # Count occurrences of each race among unarmed shootings
    unarmed_race_counts = {}
    for entry in unarmed_selection.values():
        race = entry['race']
        if race not in unarmed_race_counts:
            unarmed_race_counts[race] = 0
        unarmed_race_counts[race] += 1

    # Print fraction of unarmed shootings with a Black subject
    unarmed_black_fraction = unarmed_race_counts.get('B', 0) / len(unarmed_selection)
    print("Fraction of unarmed shootings with a Black subject:", unarmed_black_fraction)

if __name__ == "__main__":
    main()