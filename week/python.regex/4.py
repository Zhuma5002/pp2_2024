import re
def txt_match(txt):
    patterns="[A-Z]+[a-z]+$"
    if re.search(patterns, txt):
        return "Found a match"
    else:
        return "Not matched"
print(txt_match("aaAaab"))
print(txt_match("aaaaB"))
print(txt_match("Aaab"))