import re
txt="That will be 342 dollars"
x=re.findall("\d", txt)
print(x)