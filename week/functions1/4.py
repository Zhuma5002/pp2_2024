#get prim num:
def filter_prime(n):
    if n<2:
        return False
    for i in range (2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
prime_list=[x for x in range(2,200) if filter_prime(x)]
print(prime_list)