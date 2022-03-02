def get_dict(filename):
    """
    Convert the contents of the file into a dict

    Argument:
        filename: string, path of the file
    Return:
        result: dict; keys are strings, values are integers
    """
    f=open(filename,'r')
    s=f.readlines()[1:]
    a={}
    f.close()
    for e in s:
        x=e.split(',')
        a[x[0]]=int(x[1])
    return a