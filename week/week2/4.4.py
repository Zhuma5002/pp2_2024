# remove list items

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # remove "banana"

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # another method remove of second item with pop
# if you dont specify the index, the pop() method removes the last item.
# del keyword also removes specified inndex

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # The clear() method empties the list. 