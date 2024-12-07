# Task 1: Understanding the data

# Question 1:
# Summary of the data: The data includes information on fatal police shootings compiled by the Washington Post. It consists of details such as the date, threat type, armed status, demographics, location, and other related information. The data is publicly available on GitHub.

# Question 2:
# Column information:
# - id: Unique identifier for each entry.
#   Examples: 3, 325, 8853
# - date: Date of the incident.
#   Examples: 2015-01-02, 2023-01-11
# - threat_type: Type of threat encountered by police.
#   Examples: point, move, attack
# - flee_status: Fleeing status of the subject.
#   Examples: not, car, other
# - armed_with: Weapon the subject was armed with.
#   Examples: gun, unarmed, replica
#   ... (repeat for other columns)

# Question 3:
# Percent of the US population that is black: According to the most recent data, around 13.4% of the US population is Black. (Source: United States Census Bureau)

### task2.py ###
# Task 2: Reading the data into a dictionary

# Question 1:
# Information stored in database: The columns stored in the database are 'name', 'date', 'armed', 'age', 'gender', 'race', and 'state'.

# Question 2:
# Keys in database: The keys in the dictionary database are the unique identifiers (id) of each entry.

# Question 3:
# Type of values in database: The values in the database are dictionaries.

# Question 4:
# Information stored in a value: Each value in the database stores details about each fatal police shooting entry. For example, database[3] would contain information like the name, date, armed status, age, gender, race, and state of the subject.

### task3.py ###
# Task 3: Using the database

# Question 1:
# Comparison of black subjects: The proportion of black subjects in fatal police shootings will be compared to the representation of Black people in the US population.

# Question 2:
# Comparison of unarmed black subjects: The proportion of black subjects in fatal police shootings where the subject is unarmed will be compared to the representation of Black people in the US population and to the proportion of black subjects in all police shootings.

### task4.py ###
# Task 4: Reflection

# Question 1:
# Reflection: This project provided insights into analyzing real-world data using Python dictionaries. It highlighted disparities in fatal police shootings and raised awareness about racial demographics in such incidents. Working with the data was eye-opening and emphasized the importance of data-driven discussions on social issues.