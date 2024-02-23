import re
txt="fdskfdj nndjfn, fe,"
x=re.sub("[ ,.]",":", txt)
print(x)