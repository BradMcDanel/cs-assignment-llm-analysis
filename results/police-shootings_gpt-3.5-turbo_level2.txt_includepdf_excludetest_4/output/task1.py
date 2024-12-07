# Task 1: Understanding the data

# Question 1:
# The data on fatal police shootings includes information such as the date, threat type, flee status, armed status, city, state, location coordinates, subject's name, age, gender, race, mental illness status, body camera usage, and agency IDs. The data comes from the Washington Post's compilation of fatal police shootings.

# Question 2:
# - Column headers: id, date, threat_type, flee_status, armed_with, city, county, state, latitude, longitude, location_precision, name, age, gender, race, race_source, was_mental_illness_related, body_camera, agency_ids
# - Information in the columns: The 'id' column contains unique identifiers for each entry. For example, some values in the 'id' column are 3, 4, 5. The 'date' column stores the date of the incident. The 'threat_type' column indicates the type of threat posed by the subject.
# - Examples:
#   - id: 3, date: 2015-01-02, threat_type: point
#   - id: 4, date: 2015-01-02, threat_type: point
#   - id: 5, date: 2015-01-03, threat_type: move

# Question 3:
# The percentage of the United States population that is black is approximately 13.4%. (Source: U.S. Census Bureau, 2019)

### task2.py ###
# Task 2: Reading the data into a dictionary

# Question 1:
# The columns used from the dataset are 'name', 'date', 'armed', 'age', 'gender', 'race', 'state'.

# Question 2:
# The keys in the dictionary database are the unique identifiers (id) of each entry.

# Question 3:
# The type of the values in the database dictionary is dictionary.

# Question 4:
# Example value in database:
# Key: 3
# Value: {'name': '2015-01-02', 'date': 'point', 'armed': 'not', 'age': 'gun', 'gender': 'Shelton', 'race': 'Mason', 'state': 'WA'}

### task3.py ###
# Task 3: Using the database

# Question 1:
# The proportion of black subjects in fatal police shootings is compared to the representation of black people in the United States population by calculating the fraction of fatal police shootings with a black subject.

# Question 2:
# The proportion of black subjects in fatal police shootings where the subject is unarmed is compared to the representation of black people in the United States population and with the proportion of black subjects in all police shootings.

### task4.py ###
# Task 4: Reflection

# Question 1:
# (Your reflection here)