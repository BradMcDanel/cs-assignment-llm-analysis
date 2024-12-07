# This script reads the data from "fatal-police-shootings-data.csv" file and organizes it into a Python dictionary named database.
# Each entry in the database dictionary contains information about the subject of a fatal police shooting, such as name, date, armed status, age, gender, race, and state.

### write-up.txt ###
# Task 1, write your answers to the corresponding questions.
# Question 1: The data includes information on fatal police shootings and is sourced from the Washington Post's compilation.
# Question 2: - Column headers: id, date, threat_type, flee_status, armed_with, city, county, state, latitude, longitude, location_precision, name, age, gender, race, race_source, was_mental_illness_related, body_camera, agency_ids
#              - Example values: id - 3, date - 2015-01-02, threat_type - point, flee_status - not, armed_with - gun
# Question 3: The percentage of the United States population that is black is approximately 13.4% (U.S. Census Bureau).

# Task 2, write your answers to the corresponding questions.
# Question 1: The information stored in the database includes columns: name, date, armed, age, gender, race, and state.
# Question 2: The keys in the database are the IDs of the fatal police shooting incidents.
# Question 3: The values in the database are dictionaries containing details about each fatal police shooting incident.
# Question 4: Example value in the database: {'name': 'Tim Elliot', 'date': '2015-01-02', 'armed': 'gun', 'age': '53', 'gender': 'male', 'race': 'A', 'state': 'WA'}

# Task 3, write your answers to the corresponding questions.
# Question 1: The proportion of black subjects in fatal police shootings is compared to the representation of black people in the United States population, showing disparities.
# Question 2: The proportion of black subjects in fatal police shootings where the subject is unarmed is compared to the representation of black people in the U.S. population and all police shootings.

# Task 4, write your answers to the corresponding question.
# Question 1: This project provided valuable insights into analyzing real-world data using Python dictionaries. It highlighted disparities in fatal police shootings and the importance of data analysis in understanding social issues.

### fatal-police-shootings-data.csv ###
# Contains data on fatal police shootings, including columns: id, date, threat_type, flee_status, armed_with, city, county, state, latitude, longitude, location_precision, name, age, gender, race, race_source, was_mental_illness_related, body_camera, agency_ids
# Example entries: id - 3, date - 2015-01-02, threat_type - point, flee_status - not, armed_with - gun, city - Shelton, county - Mason, state - WA

### test_police_shootings.py ###
# Contains pytest tests for the Python script police_shootings.py to ensure correct functionality and outputs.