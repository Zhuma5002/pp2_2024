import re

txt="Hello planet"
#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
x=re.findall("He.*o", txt)
print(x)