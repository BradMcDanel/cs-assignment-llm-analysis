def format_predator_eats(predator, prey_list):
    if len(prey_list) == 0:
        return f"{predator} eats nothing"
    elif len(prey_list) == 1:
        return f"{predator} eats {prey_list[0]}"
    else:
        return f"{predator} eats {', '.join(prey_list[:-1])} and {prey_list[-1]}"