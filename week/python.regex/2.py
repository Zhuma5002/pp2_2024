#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
def txt_match(txt):
    patterns="ab{2,3}"
    if re.search(patterns, txt):
        return "Found a match"
    else:
        return "Not matched"
print(txt_match("abb")) 
print(txt_match("abbb"))    
print(txt_match("abbbb"))  
print(txt_match("abc"))      