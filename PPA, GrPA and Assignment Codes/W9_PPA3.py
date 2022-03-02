# My own code:-
def get_max_line(filename):
    """
    Get the line that houses the maximum value

    Argument:
        filename: string, path to the file
    Return:
        result: integer
    """
    f=open(filename,'r')
    s=f.readlines()
    f.close()
    max=int(s[0])
    for line in s:
        if(int(line)>max):
            max=int(line)
    for i in range(0,len(s)-1):
        if(int(s[i])==max):
            return i+1
    return int(s[0])

'''
#IITM Solution Code:-
def get_max_line(filename):
    f = open(filename, 'r')
    line = f.readline()
    maxnum, maxline = int(line.strip()), 1
    count = 1
    for line in f:
        num = int(line.strip())
        count += 1
        if num > maxnum:
            maxnum = num
            maxline = count
    return maxline
'''