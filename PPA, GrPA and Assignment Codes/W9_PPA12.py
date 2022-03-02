def write_pattern(n):
    """
    Write a pattern to file

    Argument:
        n: integer
    Return:
        None
    """
    x=[]
    for i in range(n):
        s=[]
        for j in range(n):
            if(i==j):
                s.append(1)
            elif((i+j)==n-1):
                s.append(1)
            else:
                s.append(0)
        x.append(s)
    f=open('pattern.csv','w')
    for each in x:
        a=''
        for i in range(n):
            if(i==n-1):
                a=a+str(each[i])+'\n'
            else:
                a=a+str(each[i])+','
        f.write(a)
    f.close()

write_pattern(7)