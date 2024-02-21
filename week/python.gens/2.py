def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1


n=int(input('inter the numbber of value n'))
data=[]
for i in EvenGenerator(n):
    data.append(str(i))

print (",".join(data))