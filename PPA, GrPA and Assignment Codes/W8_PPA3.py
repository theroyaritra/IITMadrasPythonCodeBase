def multiply(a, b):
    """
    A recursive function to compute the product of two numbers

    Arguments:
        a, b: integers
    Return:
        result: integer
    """
    if(b==0):
        return 0
    elif(b==1):
        return a
    return a+multiply(a,b-1)

print(multiply(7,8))