# if, else

a = 33
b = 200
if b > a:
  print("b is greater than a")

  a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal") #The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b") # The else keyword catches anything which isn't caught by the preceding conditions.

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") #You can also have an else without the elif

a = 200
b = 33
if a > b: print("a is greater than b") #one line statement

a = 2
b = 330
print("A") if a > b else print("B")