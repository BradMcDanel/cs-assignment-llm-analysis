# Import the necessary modules
import police_shootings

def print_name_with_id(database, id_num):
    print(database[id_num]["name"])

def print_all_names_in_state(database, state):
    for key, value in database.items():
        if value["state"] == state:
            print(value["name"])

def count_race_occurrences(database):
    race_counts = {}
    for value in database.values():
        race = value["race"]
        if race in race_counts:
            race_counts[race] += 1
        else:
            race_counts[race] = 1
    return race_counts

def calculate_black_fraction(race_counts):
    total_shootings = sum(race_counts.values())
    black_shootings = race_counts.get("B", 0)  # Assuming 'B' represents black race
    black_fraction = black_shootings / total_shootings
    return black_fraction

def filter_unarmed_shootings(database):
    unarmed_selection = {k: v for k, v in database.items() if v["armed"] == "unarmed"}
    return unarmed_selection

def count_unarmed_race_occurrences(unarmed_selection):
    unarmed_race_counts = {}
    for value in unarmed_selection.values():
        race = value["race"]
        if race in unarmed_race_counts:
            unarmed_race_counts[race] += 1
        else:
            unarmed_race_counts[race] = 1
    return unarmed_race_counts

def calculate_unarmed_black_fraction(unarmed_race_counts):
    total_unarmed_shootings = sum(unarmed_race_counts.values())
    black_unarmed_shootings = unarmed_race_counts.get("B", 0)  # Assuming 'B' represents black race
    black_unarmed_fraction = black_unarmed_shootings / total_unarmed_shootings
    return black_unarmed_fraction

if __name__ == "__main__":
    print_name_with_id(police_shootings.database, 1694)
    print_all_names_in_state(police_shootings.database, "Minnesota")
    race_counts = count_race_occurrences(police_shootings.database)
    black_fraction = calculate_black_fraction(race_counts)
    print(black_fraction)
    unarmed_selection = filter_unarmed_shootings(police_shootings.database)
    unarmed_race_counts = count_unarmed_race_occurrences(unarmed_selection)
    black_unarmed_fraction = calculate_unarmed_black_fraction(unarmed_race_counts)
    print(black_unarmed_fraction)