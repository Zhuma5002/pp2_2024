import re

txt="Hello Zhuma"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x=re.findall("H...o",txt)
print(x)