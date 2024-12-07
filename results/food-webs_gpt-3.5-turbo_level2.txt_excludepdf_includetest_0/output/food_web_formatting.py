def format_output(items):
    if len(items) == 0:
        return "(None)"
    elif len(items) == 1:
        return items[0]
    else:
        return ", ".join(items[:-1]) + " and " + items[-1]