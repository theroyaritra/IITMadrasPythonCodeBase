def relation(file1, file2):
    """
    Determine the relationship between two files

    Arguments:
        file1, file2: strings, paths to two files
    Return:
        string: 'Equal', 'Subset' or 'No Relation'
    """
    f1=open(file1,'r')
    f2=open(file2,'r')
    s1=f1.readlines()
    s2=f2.readlines()
    f1.close()
    f2.close()
    if(len(s1)==len(s2)):
        f=True
        for i in range(len(s1)):
            if(s1[i].strip()!=s2[i].strip()):
                f=False
                break
        if(f):
            return "Equal"
    else:
        if(s1<s2):
            l=len(s1)
        else:
            l=len(s2)
        f=True
        for i in range(l):
            if(s1[i].strip()!=s2[i].strip()):
                f=False
                break
        if(f):
            return "Subset"
    return "No Relation"