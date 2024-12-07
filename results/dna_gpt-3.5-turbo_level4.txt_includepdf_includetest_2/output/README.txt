Please find the implementation of the DNA profiling program in the respective files.
The program reads a CSV file containing STR counts for individuals and a text file containing a DNA sequence to identify the owner.
The main entry point is in profile.py, which can be run from the command line with the CSV file and DNA sequence file as arguments.
The program will output the name of the individual to whom the DNA sequence most likely belongs or "No match" if there is no match.
The test_profile.py file contains unit tests to verify the correctness of the program for different scenarios.