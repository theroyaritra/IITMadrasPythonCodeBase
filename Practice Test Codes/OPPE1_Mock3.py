def matrix_type(M):
    """
    Determine the type of the matrix

    Argument:
        M: list of lists
    Return:
        mtype: str
    """
    d, sc, id = True, True, True
    s = ''
    x = M[1][1]
    for i in range(len(M)):
        for j in range(len(M[i])):
            if(i!=j and M[i][j]!=0):
                d=False
                break
    for i in range(len(M)):
        if(x != M[i][i]):
            sc = False
        if(M[i][i] != 1):
            id = False
    if(d):
        s = "diagonal"
    else:
        s="non-diagonal"
    if(d == True and sc == True):
        s = "scalar"
    if(d == True and id == True):
        s = "identity"
    return s


print(matrix_type([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))  # identity
print(matrix_type([[4, 0, 0], [0, 4, 0], [0, 0, 4]]))  # scalar
print(matrix_type([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 52, 0], [0, 0, 0, 1]])) #diagonal
print(matrix_type([[1, 0, 0, 0], [0, 2, 0, 0],[0, 0, 3, 0], [0, 0, 0, 4]]))  # diagonal
print(matrix_type([[1, 2, 3], [4, 9, 56], [2, 7, 8]])) #non-diagonal
