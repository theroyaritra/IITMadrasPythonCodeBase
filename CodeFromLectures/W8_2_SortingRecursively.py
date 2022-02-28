def findMin(L):
    min=L[0]
    for e in L:
        if(e<min):
            min=e
    return min

def findMax(L):
    max=L[0]
    for e in L:
        if(e>max):
            max=e
    return max

def AscendingSort(L):
    if(L==[] or len(L)==1):
        return L
    else:
        m=findMin(L)
        L.remove(m)
        return [m]+AscendingSort(L)

def DescendingSort(L):
    if(L==[] or len(L)==1):
        return L
    else:
        m=findMax(L)
        L.remove(m)
        return [m]+DescendingSort(L)

print(DescendingSort([54,85,96,-98,69,52.25,65.5,-695.55]))
print(AscendingSort([54,85,96,-98,69,52.25,65.5,-695.55]))