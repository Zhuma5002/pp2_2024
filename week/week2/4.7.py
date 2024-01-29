#sort lists

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) # List objects have a sort() method that will sort the list alphanumerically, ascending, by default

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) # sort numerically

# to sort descendin: "reverse=true":
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)