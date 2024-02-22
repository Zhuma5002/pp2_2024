import re
txt="privet mir"
x=re.findall("privet$", txt)
if x:
    print("string starts wiith privet")
else:
    print("no match")