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