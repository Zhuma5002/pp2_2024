# list comprehesion

list=["adwdewdw", "bgtrtr","ctgtgttg"]
newlist=[]

for x in list:
    if "t" in x:
        newlist.append(x)

print(newlist) #List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# output: ['bgtrtr',ctgtgttg'] 

