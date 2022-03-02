def add_period(filename):
    """
    Add a period at the end of each line

    Argument:
        filename: string; path of the file
    Return:
        None
    """
    f=open(filename,'r')
    x=open("out.txt",'w')
    for line in f:
        line=line.strip()
        x.write(line+'.'+'\n')
    f.close()
    x.close()

add_period('myText.txt')