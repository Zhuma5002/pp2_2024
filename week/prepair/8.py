#spy_game:
def spy_game(n):
        for i in range(0, len(n)):
                if n[i]==0:
                   for j in range(i+1,len(n)):
                         if n[j]==0:
                            for k in range(i+2, len(n)):
                                  if n[k]==7:
                                      return 1
                                  return 0
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))