# Your code here

import re
def valid_password(password):
    string = list(password)
    for char in string:
        if not (6 < len(string) < 12): 
            return "Invalid password. Please try again"
        if (re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[0-9]", password) and re.search("[$#@]", password)):
            return "Valid password"
        else:
            return "Invalid password. Please try again"
        
        
    
    


print(valid_password("ABd1234@1") )