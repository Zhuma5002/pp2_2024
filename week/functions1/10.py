# unique el:
def list(s):

    x = []
    for a in s:
       if a not in x:
           x.append(a) 
    return x

print(list([1,1,1,1,2,2,2,2,3,4,5,6,6,6,6])) 
