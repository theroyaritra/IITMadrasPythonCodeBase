# My solution code:-
def get_freq(filename):
    """
    Extract frequency information from the file

    Argument:
        filename: string, path to file
    Return:
        result: dictionary; keys are strings, values are integers
    """
    f=open(filename,'r')
    s=f.readlines()
    f.close()
    a={}
    for line in s:
        if(line.strip() in a):
            a[line.strip()]+=1
        else:
            a[line.strip()]=1
    return a

'''
#IITM Solution Code:-
def get_freq(filename):
    f = open(filename, 'r')
    freq = dict()
    for line in f:
        word = line.strip()
        if word not in freq:
            freq[word] = 0
        freq[word] += 1
    f.close()
    return freq
'''