def num_to_words(mat):
    """
    Convert matrix to file

    Argument: 
        mat: list of lists
    Return:
        None
    """
    a={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
    f=open('words.csv','w')
    for e in mat:
        s=''
        for i in range (len(e)):
            s+=a[e[i]]+","
        s=s.rstrip(',')
        s=s+'\n'
        f.write(s)
    f.close()