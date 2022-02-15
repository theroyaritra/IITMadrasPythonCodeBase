# My own code:-
def merge(D1, D2, priority):
    """
    Merge two dicts

    Arguments: 
        - D1: first dictionary
        - D2: second dictionary
        - priority: string
    Returns: D; merged dictionary
    """
    D={}
    x,y=set(D1.keys()),set(D2.keys())
    common=x.intersection(y)
    for e in common:
        if(priority=="first"):
            D[e]=D1[e]
        else:
            D[e]=D2[e]
        D1.pop(e)
        D2.pop(e)
    for e in D1:
        D[e]=D1[e]
    for e in D2:
        D[e]=D2[e]
    return D

#IIT Madras solution code:-
'''
# The basic idea is to write the code for priority equal to "first"
# When priority is "second", we can just reverse the order of the dicts
def merge(D1, D2, priority):
    if priority == 'second':
        return merge(D2, D1, 'first')
    D = dict()
    # First copy all key-value pairs in D1 to D
    for key in D1:
        value = D1[key]
        D[key] = value
    # Copy all those key-value pairs in D2 to D
    # where the key is not already present in D
    for key in D2:
        value = D2[key]
        if key not in D:
            D[key] = value
    return D
'''
D1={1: 2, 2: 3, 3: 4}
D2={1: 10, 4: 15, 5:10}
print(merge(D1,D2,'first'))