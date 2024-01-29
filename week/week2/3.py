#python assignment operators

x=5
x+=5
print(x)

x=5
x*=5
print(x)

x=5
x%=3
print(x) #takes a remainder

x=5
x**=3
print(x) # takes five to the third power

x=5
x^=3
print(x) # 5=101, 3=11 so, 101xor11=110, 110=6.

x=5
x//=3
print(x) #This operator is used to divide the left operand with the right operand and then assigning the result(floor) to the left operand.

x=5
x&=3
print(x) # bitwise and operator. 5=101, 3=11. 101and11=001=1

x=5
x|=3
print(x) # bitwise or opeator. 5=101, 3=11. 101or11=111=7

x=5
x>>=3
print(x) # This operator is used to perform Bitwise right shift on the operands and then assigning result to the left operand.

x=5
x<<=3
print(x) #This operator is used to perform Bitwise left shift on the operands and then assigning result to the left operand.

#comprison operators:

x = 5
y = 3
print(x == y) # returns False because 5 is not equal to 3

x = 5
y = 3
print(x != y) # returns True because 5 is not equal to 3

x = 5
y = 3
print(x > y) # returns True because 5 is greater than 3

x = 5
y = 3
print(x >= y) # returns True because five is greater, or equal, to 3

#logical operators:

#and:
x = 7
print(x > 3 and x < 10) # returns True because 5 is greater than 3 AND 5 is less than 10

#or:
x = 5
print(x > 3 or x < 4) # returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

#not:
x = 5
print(not(x > 3 and x < 10)) # returns False because not is used to reverse the result

#identify operators:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) # returns True because z is the same object as x
print(x is y) # returns False because x is not the same object as y, even if they have the same content
print(x == y) # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z) # returns False because z is the same object as x
print(x is not y) # returns True because x is not the same object as y, even if they have the same content
print(x != y) # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
