def transpose(mat):
    """
    compute the transpose of the matrix

    Argument:
        mat: list of lists
    Return:
        mat_trans: list of lists
    """
    tmat=[]
    row=len(mat)
    col=len(mat[0])
    for i in range(col):
        m1=[]
        for j in range(row):
            m1.append(mat[j][i])
        tmat.append(m1)
    
    return tmat

m=[[1,2,3],[4,5,6]]
print(transpose(m))