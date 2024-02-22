# \A	Returns a match if the specified characters are at the beginning of the string
import re


txt="The rain in Spain"
x=re.findall("\AThe", txt)
print(x)

if x:
    print("yes, match")
else:
    print("no match")


#\b	Returns a match where the specified characters are at the beginning or at the end of a word(the "r" in the beginning is making sure that the string is being treated as a "raw string")
txt="The rain in Spain"
#Check if "ain" is present at the beginning of a WORD:
x=re.findall(r"\bain", txt)
print(x)
if x:
    print("yes")
else:
    print("no")


txt="The rain in Spain"
#Check if "ain" is present at the end of a WORD:
x=re.findall(r"ain\b", txt)
print(x)
if x:
    print("yes")
else:
    print("no")


#\d	Returns a match where the string contains digits (numbers from 0-9)
txt="The rain in5 Spain"
#Check if the string contains any digits (numbers from 0-9):
x=re.findall("\d",txt)
print(x)
if x:
    print("yes")
else:
    print("no")

#\d	Returns a match where the string does not contains digits (numbers from 0-9)
txt="The rain in5 Spain"
#Return a match at every no-digit character:
x=re.findall("\D",txt)
print(x)
if x:
    print("yes")
else:
    print("no")


#\s	Returns a match where the string contains a white space character
txt="The rain in5 Spain"
#Return a match at every white-space character:
x=re.findall("\s",txt)
print(x)
if x:
    print("yes")
else:
    print("no")


#\S	Returns a match where the string DOES NOT contain a white space character
txt="The rain in5 Spain"
#Return a match at every NON white-space character:
x=re.findall("\S",txt)
print(x)
if x:
    print("yes")
else:
    print("no")


#\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
txt = "The rain in Spain"
#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character)
x = re.findall("\w", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


#\W	Returns a match where the string DOES NOT contain any word characters
txt = "The rain in Spain"
#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
x = re.findall("\W", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

  
#\Z	Returns a match if the specified characters are at the end of the string
txt="The rain in Spain"
#Check if the string ends with "Spain":
x=re.findall("Spain\Z",txt)
print(x)
if x:
    print("yes!")
else:
    print("no!")
    