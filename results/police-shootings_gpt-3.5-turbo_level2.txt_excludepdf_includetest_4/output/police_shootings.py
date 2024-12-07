# This file contains the code to read the data from fatal-police-shootings-data.csv and organize it into a Python dictionary.
# The provided code reads the data from the CSV file and stores it in a dictionary named 'database'.
# The 'database' dictionary has each row from the CSV file as a key-value pair, where the key is the ID of the shooting incident and the value is a dictionary containing the details of that incident.

# Answer to Question 1:
# The information from the file fatal-police-shootings-data.csv that is stored in the 'database' dictionary includes columns like 'id', 'name', 'date', 'manner_of_death', 'armed', 'age', 'gender', 'race', 'city', 'state', 'signs_of_mental_illness', 'threat_level', etc.

# Answer to Question 2:
# The keys in the 'database' dictionary are the 'id' column values from the CSV file, representing the unique ID of each shooting incident.

# Answer to Question 3:
# The type of the values in the 'database' dictionary is dictionary. This can be found using the type(database[key]) where 'key' is an example key in the 'database' dictionary.

# Answer to Question 4:
# Looking at one of the values in the 'database' dictionary, for example, database[1694], it stores the details of the shooting incident with ID 1694.
# The value is another dictionary containing information like 'name', 'date', 'manner_of_death', 'armed', 'age', 'gender', 'race', 'city', 'state', 'signs_of_mental_illness', 'threat_level', etc.