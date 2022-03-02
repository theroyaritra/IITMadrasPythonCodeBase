def write_AP(a_1, d, n):
    """
    Write the AP to a file

    Arguments:
        a_1: first term, integer
        d: common difference, integer
        n: number of terms, integer
    Return:
        None
    """
    x=[]
    x.append(a_1)
    for i in range(1,n+1):
        if(len(x)==n):
            break
        x.append(a_1+i*d)
    f=open('out.txt','w')
    for e in x:
        f.write(str(e)+"\n")
    f.close()

write_AP(16,9,10)