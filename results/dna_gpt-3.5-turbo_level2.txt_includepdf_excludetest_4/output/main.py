# You can use this script to run the profile.py script with the provided test cases

import os

test_files = ['charlie.txt', 'nomatch.txt', 'alice.txt', 'bob.txt']
csv_file = 'data.csv'

for file in test_files:
    os.system(f'python profile.py {csv_file} {file}')