def format_prey_list(prey_list):
    if len(prey_list) == 1:
        return prey_list[0]
    else:
        return ', '.join(prey_list[:-1]) + ' and ' + prey_list[-1]