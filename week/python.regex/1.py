#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
def txt_match(txt):
    patterns="^a(b*)$"
    if re.search(patterns, txt):
        return "Found a match"
    else:
        return "Not matched"
print(txt_match("abb")) 
print(txt_match("acb"))    

