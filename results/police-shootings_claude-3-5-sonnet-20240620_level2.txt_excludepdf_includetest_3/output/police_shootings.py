import csv

# Initialize an empty dictionary to store the data
database = {}

# Open the CSV file containing the police shooting data
with open('fatal-police-shootings-data.csv', 'r') as f:
    # Create a CSV reader object
    reader = csv.DictReader(f)
    
    # Iterate through each row in the CSV file
    for row in reader:
        # Use the 'id' column as the key for our database dictionary
        key = row['id']
        
        # Create a dictionary to store relevant information for each shooting
        value = {
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
        
        # Add the key-value pair to our database dictionary
        database[key] = value

# The database dictionary is now populated with the data from the CSV file

# Task 3 code will be added here