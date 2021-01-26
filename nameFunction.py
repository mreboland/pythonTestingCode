# A simple function that takes a first and last name, returning it formatted
def getFormattedName(first, last, middle=""):
    """Generate a neatly formatted full name."""
    # Added middle name to break testing
    if middle:
        fullName = f"{first} {middle} {last}"
    else:
        fullName = f"{first} {last}"
    return fullName.title()

