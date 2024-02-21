def gensquares(n):
    for i in range(n):
        yield i**2
g=gensquares(10)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))