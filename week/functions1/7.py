#has=33:
def my_func(n):
    for i in range(len(n)-1):
        if n[i]==3 and n[i+1]==3:
           return 1
    return 0
print(my_func([1, 3, 3]))
print(my_func([1, 3, 1, 3]))
print(my_func([3, 1, 3]))