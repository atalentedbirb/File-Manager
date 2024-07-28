import re

def no_no_folder_windows(string):
    pattern = r"^C:\\Windows.*" 
    # Compile the regex pattern
    regex = re.compile(pattern, re.IGNORECASE)
    # Use re.search to check if the pattern is anywhere in the string
    search = regex.search(string)
    # Return True if match is found, otherwise False
    if search:
        return True
    else:
        return False

