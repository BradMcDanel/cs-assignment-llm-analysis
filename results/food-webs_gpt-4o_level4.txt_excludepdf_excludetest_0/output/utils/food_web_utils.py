def format_predator_prey(predator, prey_list):
    """Format the predator and its prey for display."""
    if not prey_list:
        return f"{predator} eats nothing"
    if len(prey_list) == 1:
        return f"{predator} eats {prey_list[0]}"
    return f"{predator} eats {', '.join(prey_list[:-1])} and {prey_list[-1]}"