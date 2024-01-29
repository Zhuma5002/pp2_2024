#sets

thisset = {"apple", "banana", "cherry"}
print(thisset) # the set list is unordered, meaning: the items will appear in a random order.

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) # dublicates not allowed

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset) #The values True and 1 are considered the same value in sets, and are treated as duplicates

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

set1 = {"abc", 34, True, 40, "male"} # set can contain different data types

myset = {"apple", "banana", "cherry"}
print(type(myset))