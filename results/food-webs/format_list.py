def formatList(data):
    if len(data) == 0:
        return "(None)"
    
    retval = ""
    for i in range(0, len(data) - 2):
        retval = retval + str(data[i]) + ", "
    if len(data) >= 2:
        retval += str(data[-2]) + " and "
    retval += str(data[-1])
    
    return retval

if __name__ == "__main__":
    values = ["Alice", "Bob", "Chad", "Diane"]
    print(values, "is formatted as", formatList(values))