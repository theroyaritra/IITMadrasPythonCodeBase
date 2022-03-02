#My own code:-
def read_line(filename, n):
    """
    Read the nth line of the file

    Argument:
        filename: string, name of the file to be read
    Return:
        string: return nth line of the file
    """
    f=open(filename,'r')
    s=f.readlines()
    f.close()
    if(n>len(s)):
        return None
    return (s[n-1].strip())
'''
#IITM Solution Code:
def read_line(filename, n):
    f = open(filename, 'r')
    count = 0
    line = f.readline()
    while line != '':
        count += 1
        line = line.strip()
        if count == n:
            return line
        line = f.readline()
    f.close()
    return None
'''

print(read_line("mytext.txt",5))