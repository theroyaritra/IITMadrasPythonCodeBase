def prime(n):
    f=True
    if n==2:
        return f
    if n==0 or n==1:
        return False
    for i in range(2,n):
        if(n%i==0):
            f=False
            break
    return f
def primes_galore(L):
    c=0
    for i in range(len(L)):
        if(prime(i) and prime(L[i])):
            c=c+1
    return c

print(primes_galore([1, 3, 11, 18, 17, 5, 6, 8, 10]))
print(primes_galore([1, 2, 3, 4, 5, 6, 7, 8, 9]))