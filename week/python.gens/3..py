def func(n):
    num = 0
    while num <= n:
        if num % 3 == 0 and num % 4 == 0:
            yield num
        num += 1
v = int(input())

for i in func(v):
    print(i, end = " ")