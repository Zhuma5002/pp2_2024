import os

path = r"\Users\Админ\Documents\kbtu\pp2_2024\week\dir-and-files"

with os.scandir(path) as it:
    for x in it:
        if(x.is_dir()):
            print(x.name)
print(" ")
with os.scandir(path) as it:
    for x in it:
        if(not x.is_dir()):
            print(x.name)
print(" ")
with os.scandir(path) as it:
    for x in it:
        print(x.name)