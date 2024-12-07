def format_predator_and_prey(predator, prey_list):
    if len(prey_list) == 1:
        return f"{predator} eats {prey_list[0]}"
    elif len(prey_list) == 2:
        return f"{predator} eats {prey_list[0]} and {prey_list[1]}"
    else:
        return f"{predator} eats {', '.join(prey_list[:-1])} and {prey_list[-1]}"