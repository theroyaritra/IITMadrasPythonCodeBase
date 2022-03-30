def survival(T):
    """
    Determine if the organism will survive or not
    
    Argument:
        T: integer
    Return:
        result: bool
    """
    f=False
    for x in range(6):
        for y in range(6):
            m=30+x**2+y**2-3*x-4*y
            if(m<=T):
                f=True
                break
    return f
    