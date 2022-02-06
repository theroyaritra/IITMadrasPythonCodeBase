def fibo(n):
    """
    compute the nth fibonacci integer
	
    Argument:
        n: int
    Return:
        f_n: int
    """
    if(n==1 or n==2):
        return 1
    else:
        return (fibo(n-1)+fibo(n-2))

print(fibo(10))
print(fibo(3))