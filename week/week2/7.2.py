# change items

car={"brand":"range rover", "model":"sport", "year":"2023"}
car["year"]="2013"
print(car)

car={"brand":"range rover", "model":"sport", "year":"2023"}
car.update({"year": 2013})
print(car)