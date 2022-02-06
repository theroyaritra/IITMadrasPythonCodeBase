def first_three(L):
    """
    computes the first three maximums

    Argument:
        L: list
    Return:
        fmax, smax, tmax: three integers
    """
    x = []
    for i in range(0, 3):
        max=L[0]
        for e in L:
            if(e > max):
                max = e
        x.append(max)
        L.remove(max)
    return x

print(first_three([90,2,3,4,5,6,52,8]))