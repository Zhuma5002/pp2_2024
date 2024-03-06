#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
str=input()
ucount=0
lcount=0
for x in str:
    if(ord(x)>=65 and ord(x)<=90):
        ucount+=1
    if(ord(x)>=97 and ord(x)<=122):
        lcount+=1
print(ucount)
print(lcount)