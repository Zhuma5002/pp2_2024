# add list items

thislist = ["apple", "banana", "cherry"]
thislist.append("orange") #Using the append() method to append an item
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) # Add the elements of tropical to thislist
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) #Add elements of a tuple to a list
