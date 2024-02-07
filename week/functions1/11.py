#check is palindrom:
def isPalindrome(s):
    if s==s[::-1]:
        return "ok"
    else:
        return "wtf"
s=input()
print(isPalindrome(s))