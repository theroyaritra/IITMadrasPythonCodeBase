def is_empty(L):
    return L == [ ]

def first(L):
    if is_empty(L):
        return None
    return L[0]

def last(L):
    if is_empty(L):
        return None
    return L[-1]

def init(L):
    if is_empty(L):
        return None
    return L[:-1]

def rest(L):
    if is_empty(L):
        return None
    return L[1: ]

print(first([1, 2, 3]))
print(last([1, 2, 3, 4]))
print(is_empty([ ]))
print(is_empty([1, 2]))
print(first([ ]))
print(first([-1, 10, 2]))
print(last([ ]))
print(last([10, 0, -100]))
print(init([ ]))
print(init([1, 2, 3, 4, 5]))
print(rest([ ]))
print(rest([1, 2, 3, 4, 5, 6]))

