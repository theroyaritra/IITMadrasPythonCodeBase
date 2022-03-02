#My own code:-
def read_file(filename):
    """
    Read the file and print each line

    Argument:
        filename: string, name of the file to be read
    Return:
        None
    """
    f=open(filename,'r')
    s=f.readlines()
    for e in s:
        print(e,end='')
    f.close()
'''
#IITM Solution code:-
def read_file(filename):
    f = open(filename, 'r')
    for line in f:
        print(line.strip())
    f.close()
'''