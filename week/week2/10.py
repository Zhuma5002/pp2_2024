# for loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 

for x in "mercedes":
  print(x) # looping through a string

  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break # break statement it will output apple banana
  
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) #Exit the loop when x is "banana", but this time the break comes before the print

  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) # it doesnt print banana bcz of continnue 