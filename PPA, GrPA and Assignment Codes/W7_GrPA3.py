def minor_matrix(M, i, j):
    """
    Compute the "minor matrix"

    Arguments:
        M: list of lists
        i: integer
        j: integer
    Return:
        M_ij: list of lists
    """
    M_ij = []
    for row in range(len(M)):
        # skip row i
        if row == i:
            continue
        L = [ ]
        for col in range(n):
            # skip column j
            if col == j:
                continue
            # add all other elements as they are
            L.append(M[row][col])
        M_ij.append(L)
    return M_ij