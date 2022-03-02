def improvement(filename):
    """
    Find all students who have shown an improvement
    
    Argument:
        filename: string, path to file
    Return: 
        count: integer
    """
    f=open(filename,'r')
    s=f.readlines()[1:]
    c=0
    for e in s:
        x=e.split(',')
        if(int(x[2])<int(x[3]) and int(x[3])<int(x[4])):
            c=c+1
    return c