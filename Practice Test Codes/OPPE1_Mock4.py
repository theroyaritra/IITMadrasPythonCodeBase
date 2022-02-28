def exact_count(para, n):
    """
    Determine if at least one word occurs exactly n times
    
    Arguments:
        para: string
        n: integer
    Return:
        result: bool
    """
    l=[]
    s=''
    for e in para:
        if(e!=' '):
            s=s+e
        else:
            l.append(s)
            s=''
    l.append(s)
    d={}
    for e in l:
        if(e not in d):
            d[e]=1
        else:
            d[e]+=1
    f=False
    for key in d:
        if(d[key]==n):
            f=True
            break
        else:
            f=False
    return f

print(exact_count("good word many good works good real choice",3))