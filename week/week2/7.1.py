# accessing items

dict={"brand":"Ferrari","model":"laferrari","year":"2013"}
x=dict["year"]
print(x) #Get the value of the "year" key

#There is also a method called get() that will give you the same result:
dict={"brand":"Ferrari","model":"laferrari","year":"2013"}
x=dict.get("year")
print(x)


dict={"brand":"Ferrari","model":"laferrari","year":"2013"}
x=dict.keys() # The keys() method will return a list of all the keys in the dictionary.
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

dict={"brand":"Ferrari","model":"laferrari","year":"2013"}
x=dict.values() # The values() method will return a list of all the values in the dictionary.
print(x)

#example:
car={"brand":"range rover", "model":"sport", "year":"2023"}
x=car.values()
print(x)
car["horse power"]="530hp"
print(x)