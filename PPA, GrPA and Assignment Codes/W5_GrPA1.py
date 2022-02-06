def get_range(L):
    '''
    compute the range of a list L

    Argument:
        L: list
    Return:
        range: float
    '''
    max=L[0]
    min=L[0]
    for e in L:
        if(e>max):
            max=e
        if(e<min):
            min=e
    range=(max-min)
    return range

L=[1.0,3.7,8.9,5.5,1.9,6.3,0.1,9.9]
print(get_range(L))