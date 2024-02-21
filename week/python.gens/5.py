def gfunc(n):
    num = n
    while num != 0:
        yield num 
        num -= 1

N = int(input())
for i in gfunc(N):
    print(i, end = " ")