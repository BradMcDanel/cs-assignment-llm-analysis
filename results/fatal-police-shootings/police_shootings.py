import csv

# Function to read data from CSV and populate a dictionary
def read_data(filename):
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        database = {int(row['id']): row for row in csv_reader}
    return database

# Function to find a specific shooting by ID
def find_by_id(database, id):
    return database.get(id, {}).get('name', 'Not Found')

# Function to find all shootings in a specific state
def find_by_state(database, state):
    return [details['name'] for id, details in database.items() if details['state'] == state]

# Function to count occurrences by race
def count_by_race(database):
    race_counts = {}
    for entry in database.values():
        race = entry.get('race', 'Unknown')
        race_counts[race] = race_counts.get(race, 0) + 1
    return race_counts

# Function to calculate fraction of shootings by race
def calculate_fraction(race_counts, race):
    total_shootings = sum(race_counts.values())
    shootings_of_race = race_counts.get(race, 0)
    return shootings_of_race / total_shootings if total_shootings else 0

if __name__ == '__main__':
    data_file = "fatal-police-shootings-data.csv"
    database = read_data(data_file)
    print(find_by_id(database, 1694))  # Example ID
    print(find_by_state(database, 'MN'))  # Example state
    race_counts = count_by_race(database)
    print(calculate_fraction(race_counts, 'B'))  # Example race code for Black individuals