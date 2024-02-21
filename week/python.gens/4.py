def squares(n, m):
    num = n
    while num <= m:
        yield num * num 
        num += 1

s = int(input())
v = int(input())

for i in squares(s, v):
    print(i, end = " ")