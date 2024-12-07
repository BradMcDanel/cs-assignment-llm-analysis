data_file = open("fatal-police-shootings-data.csv", 'r')
data_lines = data_file.readlines()

database = {}
for row in range(1, len(data_lines)):
    line = data_lines[row]
    entries = line.split(',')
    db_entry = {}
    db_entry["name"] = entries[1]
    db_entry["date"] = entries[2]
    db_entry["armed"] = entries[4]
    db_entry["age"] = entries[5]
    db_entry["gender"] = entries[6]
    db_entry["race"] = entries[7]
    db_entry["state"] = entries[9]
    entry_id = int(entries[0])
    database[entry_id] = db_entry