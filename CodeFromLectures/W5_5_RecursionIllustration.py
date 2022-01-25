def sum(n):
    if(n==1):
        return 1
    else:
        return n+sum(n-1)

def compound(p,n): #Calculating Compound interest assuming 10% rate of interest where p is principal and n is number of years
    if(n==1):
        return p*1.1
    else:
        return (compound(p,n-1)*1.1)

def factorial(n):
    if(n==1):
        return 1
    else:
        return (factorial(n-1)*n)

print(sum(10))
print(compound(10000,5))
print(factorial(5))