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

  for x in range(6):
   print(x) # range function 0 1 2 3 4 5

  for x in range(2, 30, 5):
   print(x) # it will putput 2 7 12 17 22 27

   for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!") # else in for loop

