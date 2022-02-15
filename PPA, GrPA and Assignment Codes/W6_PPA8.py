def factors(n):
    """
    Compute the set of factors of n
			
    Argument:
        n: integer
    Return:
        factors_of_n: set
    """
    a=[]
    for i in range(1,n+1):
        if(n%i==0):
            a.append(i)
    return set(a)

def common_factors(a, b):
    """
    Compute the set of common factors of a and b

    Arguments:
        a, b: integers
    Return:
        factors_common: set
    """
    m=[]
    x,y=factors(a),factors(b)
    m=x.intersection(y)
    return set(m)

def factors_upto(n):
    """
    Get the factors up to n 
	
    Argument:
        n: integer
    Return:
        result: dict (keys: integers, values: sets)
    """
    d= dict()
    for i in range(1,n+1):
        d[i] = factors(i)
    return d