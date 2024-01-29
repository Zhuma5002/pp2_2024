#change list items

list=["cat", "dog", "fish"]
list[1]="bear"
print(list) #change item value

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"] #Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) # Change the second and third value by replacing it with one value

list=["engine", "wheel", "fuselage", "wing"]
list.insert(3, "spoilers") # insert "spoilers" to the third item
print(list)