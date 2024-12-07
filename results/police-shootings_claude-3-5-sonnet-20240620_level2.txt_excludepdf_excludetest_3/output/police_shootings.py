import csv

# Initialize an empty dictionary to store the data
database = {}

# Open and read the CSV file
with open('fatal-police-shootings-data.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Iterate through each row in the CSV file
    for row in reader:
        # Use the 'id' column as the key for the database dictionary
        key = row['id']
        
        # Create a dictionary for each entry, storing relevant information
        database[key] = {
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

# The database dictionary is now populated with the data from the CSV file