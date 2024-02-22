import re

txt="The rain in Spain falls mainly in the plain!"
x=re.findall("falls|stays", txt)
print(x)
if x:
    print("yes!")
else:
    print("no match")