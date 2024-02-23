import re
def txt_match(txt):
    patterns="^[a-z]+_[a-z]+$"
    if re.search(patterns, txt):
        return "Found a match"
    else:
        return "Not matched"
print(txt_match("aa_aab"))
print(txt_match("aa_aaB"))
print(txt_match("aA_aab"))