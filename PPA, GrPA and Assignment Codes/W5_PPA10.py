def insert(L, x):
    """
    insert an element x into a sorted list L

    Arguments:
        L: list
        x: integers
    Return:
        sorted_L: list
    """
    list=[]
    i=0
    if(x>=L[len(L)-1]):
        for e in L:
            list.append(e)
        list.append(x)
        return(list)
    for i in range(0,len(L)):
        if(L[i]>=x):
            for j in range(0,i):
                list.append(L[j])
            list.append(x)
            break
    for j in range(i,len(L)):
        list.append(L[j])
    return list

print(insert([10],10))
print(insert([1,2,3,4,5,6,7,8,9],10))
print(insert([10,20,30,40,50,60,70,80,90,100],55))

'''
IITM Solution Code:-
def insert(L, x):
    out_L = [ ]         
    inserted = False    
    for elem in L:
        if (not inserted) and (elem > x):
            out_L.append(x)
            inserted = True
        out_L.append(elem)
    if (not inserted):
        out_L.append(x)
    return out_L
'''