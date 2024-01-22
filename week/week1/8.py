#print srings
print("Hello Zhumagali")

#assign string
x="privet mir"
print(x)

#text
x="hello everyone das ist my python practice"
print(x)

#slicing str
x="auf wiedersehen"
print(x[3:])

x="auf wiedersehen"
print(x[3:5])

x="auf wiedersehen"
print(x[:4])

#modify str

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip())

#concatenate str

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#format str

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))