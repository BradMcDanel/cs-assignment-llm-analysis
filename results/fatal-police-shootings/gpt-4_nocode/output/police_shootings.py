import csv

# Function to read the CSV data into a dictionary
def read_data(filepath):
    database = {}
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
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

# Additional code for Task 3
def analyze_data(database):
    # Task 3a: Print the name of the subject with ID 1694
    print("Name of subject with ID 1694:", database['1694']['name'])

    # Task 3b: Print names of all subjects from Minnesota
    print("Names of subjects from Minnesota:")
    for key, value in database.items():
        if value['state'] == 'MN':
            print(value['name'])

    # Task 3c: Count occurrences of each race
    race_counts = {}
    for value in database.values():
        race = value['race']
        if race in race_counts:
            race_counts[race] += 1
        else:
            race_counts[race] = 1

    # Task 3d: Print the fraction of black subjects in fatal shootings
    total_shootings = len(database)
    black_shootings = race_counts.get('B', 0)
    print("Fraction of black subjects in fatal shootings:", black_shootings / total_shootings)

# Main function to run the program
def main():
    data_path = 'fatal-police-shootings-data.csv'
    db = read_data(data_path)
    analyze_data(db)

if __name__ == "__main__":
    main()