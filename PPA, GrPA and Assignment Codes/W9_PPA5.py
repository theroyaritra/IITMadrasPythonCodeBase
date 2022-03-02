def get_matrix(filename):
    """
    Convert the contents of the file into a matrix

    Argument:
        filename: string
    Return:
        matrix: list of lists
    """
    f=open(filename,'r')
    s=f.readlines()
    f.close()
    b=[]
    for i in range(len(s)):
        a=[]
        x=s[i].split(',')
        for i in range(len(x)):
            a.append(int(x[i]))
        b.append(a)
    return b