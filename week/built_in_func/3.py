#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
str=list(input())
c=str.copy()
c.reverse()
if str==c:
    print("Palindrom")
else:
    print("ne Palindronom")