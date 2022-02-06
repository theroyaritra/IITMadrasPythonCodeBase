def get_column(mat, col):
    """
    extract a specific column from the matrix

    Arguments:
        mat: list of lists
        col: integer
    Return:
        col_list: list
    """
    x=[]
    if(col>=0):
        for i in range(0,len(mat)):
            x.append(mat[i][col])
    return x

def get_row(mat, row):
    """
    extract a specific row from the matrix
    
    Arguments:
        mat: list of lists
        row: integer
    Return:
        row_list: list
    """
    x=[]
    if(row>=0):
        x=mat[row]
    return x

print(get_column([[1, 2], [3, 4]], 0))
print(get_row([[1, 2], [3, 4]], 1))