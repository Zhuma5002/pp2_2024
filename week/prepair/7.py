#has 33:
def has_33(n):
    for i in range(len(n)-1):
        if n[i]==3 and n[i+1]==3:
            return 1
    return 0
print(has_33([1,1,3,3,3,3]))
print(has_33([1,3,4,5,3,3]))
print(has_33([1,1,1,2,3,4]))
