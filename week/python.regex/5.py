import re
def txt_match(txt):
    patterns = 'a.*?b$'
    if re.search(patterns, txt):
        return "Found a match"
    else:
        return "Not matched"
print(txt_match("adsdvsdf"))
print(txt_match("dafdfdb"))
print(txt_match("afdffsb"))