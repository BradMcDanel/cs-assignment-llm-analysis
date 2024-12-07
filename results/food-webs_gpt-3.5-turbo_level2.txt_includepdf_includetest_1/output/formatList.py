## Format a list of items so that they are comma separated and "and" appears
#  before the last item.
#  Parameters:
#    data: the list of items to format
#  Returns: A string containing the items from data with nice formatting
def formatList(data):
  # Handle the case where the list is empty
  if len(data) == 0:
    return "(None)"
  
  # Start with an empty string that we will add items to
  retval = ""

  # Handle all of the items except for the last two
  for i in range(0, len(data) - 2):
    retval = retval + str(data[i]) + ", "

  # Handle the second last item
  if len(data) >= 2:
    retval += str(data[-2]) + " and "

  # Handle the last item
  retval += str(data[-1])

  # Return the result
  return retval