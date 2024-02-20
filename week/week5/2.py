#python scope
def myfunc():
    x=300
    print(x)
myfunc()

#function inside function:
def myfunc():
    x=300
    def myinnerfunc():
        print(x)
        myinnerfunc()
myfunc()

#global scope:
x=300
def myfunc():
    print(x)
myfunc()
print(x)

#naming variables:
x=300
def myfunc():
    x=200
    print(x)
myfunc()
print(x)

#global keyword:
def myfunc():
    global x #If you use the global keyword, the variable belongs to the global scope
    x=300
myfunc()
print(x)

#Also, use the global keyword if you want to make a change to a global variable inside a function.
x=300
def myfunc():
    global x
    x=200
myfunc()
print(x)