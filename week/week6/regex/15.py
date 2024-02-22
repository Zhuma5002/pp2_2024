#Sets
#A set is a set of characters inside a pair of square brackets [] with a special meaning:

#[arn]	Returns a match where one of the specified characters (a, r, or n) is present
import re

txt = "The rain in Spain"

#Check if the string has any a, r, or n characters:

x = re.findall("[arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


txt="The rain in Spain"
x=re.findall("[a-n]", txt)
print(x)

if x:
  print("yes")
else:
  print("no")

#[^arn]	Returns a match for any character EXCEPT a, r, and n
txt="The rain in Spain"
x=re.findall("[^arn]", txt)
print(x)

if x:
  print("yes")
else:
  print("no")


#[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present
txt="The rain in Spain"
##Check if the string has any 0, 1, 2, or 3 digits:
x=re.findall("[0123]", txt)
print(x)

if x:
  print("yes")
else:
  print("no")


#[0-9]	Returns a match for any digit between 0 and 9
txt = "8 times before 11:45 AM"
#Check if the string has any digits:
x=re.findall("[0-9]", txt)
print(x)

if x:
  print("yes")
else:
  print("no")


##Check if the string has any two-digit numbers, from 00 to 59:
txt = "8 times before 11:45 AM"
x=re.findall("[0-5][0-9]", txt)
print(x)

if x:
  print("yes")
else:
  print("no")


##Check if the string has any characters from a to z lower case, and A to Z upper case:
txt = "8 times before 11:45 AM"
x=re.findall("[a-zA-Z]", txt)
print(x)

if x:
  print("yes")
else:
  print("no")


import re

txt = "8 times before 11+45 "
#Check if the string has any + characters:
x = re.findall("[+]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
