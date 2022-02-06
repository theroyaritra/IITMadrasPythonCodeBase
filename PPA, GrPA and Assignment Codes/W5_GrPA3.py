def dletter(l1,l2):
    a=b=0
    st="abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        if(l1==st[i]):
            a=i+1
        if(l2==st[i]):
            b=i+1
    diff=abs(b-a)
    return diff
def distance(word_1, word_2):
    """
    compute distance between two words

    Arguments:
        word_1, word_2: strings
    Return:
        word_distance: int
    """
    w1=word_1.lower()
    w2=word_2.lower()
    dist=0
    if(len(w1) != len(w2)):
        return -1
    else:
        for i in range(len(w1)):
            dist=dist+dletter(w1[i],w2[i])
        return dist

print(distance("dog",'cat'))
print(distance("greet","great"))
print(distance("aritra",'royal'))