# the search function
#The search() function searches the string for a match, and returns a Match object if there is a match.
#If there is more than one match, only the first occurrence of the match will be returned:

import re
txt="The rain in spain"
x=re.search("\s",txt)
print ("position:", x.start())

import re
txt="The rain in spain"
x=re.search("Kazakhstan",txt)
print (x)


#The split() Function
#The split() function returns a list where the string has been split at each match:
import re 
txt="The rain in Spain"
x=re.split("\s",txt)
print(x)


#Split the string at the first white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)


#The sub() Function
#The sub() function replaces the matches with the text of your choice:
txt = "The rain in Spain"
x = re.sub("\s","Zhuma", txt)
print(x)


txt = "The rain in Spain"
x = re.sub("\s","Zhuma", txt, 2)
print(x)



#Match Object
#A Match Object is an object containing information about the search and the result.

#The search() function returns a Match object:
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

#The Match object has properties and methods used to retrieve information about the search, and the result:

#.span() returns a tuple containing the start-, and end positions of the match.
#.string returns the string passed into the function
#.group() returns the part of the string where there was a match

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())