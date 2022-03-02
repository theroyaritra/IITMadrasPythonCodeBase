def logarithm(x):
    """
    A recursive function to compute the log of x

    Argument:
        x: integer
    Result:
        result: integer
    """
    if(x==1):
        return 0
    return 1+logarithm(x//2)

print(logarithm(1024))