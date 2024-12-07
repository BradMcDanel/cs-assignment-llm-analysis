## Format a list of items so that they are comma separated and "and" appears
#  before the last item.
#  Parameters:
#    data: the list of items to format
#  Returns: A string containing the items from data with nice formatting
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
    values = []
    print(values, "is formatted as", formatList(values))
    
    values = [1]
    print(values, "is formatted as", formatList(values))
    
    values = [3, 4]
    print(values, "is formatted as", formatList(values))
    
    values = [-1, -2, -3]
    print(values, "is formatted as", formatList(values))
    
    values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 9]
    print(values, "is formatted as", formatList(values))