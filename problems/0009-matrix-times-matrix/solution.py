def matrixmul(A:list[list[int|float]],
              B:list[list[int|float]])-> list[list[int|float]]:

    # check for empty matrices
    if not A or not B:
        return -1 
    
    # Check if matrix dimensions are compatible.
    if len(A[0])!= len(B):
        return -1
    
    # check if all rows have same length
    for row in A:
        if len(row)!= len(A[0]):
            return -1

    for row in B:
        if len(row)!= len(B[0]):
            return -1

    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    # craeting a zero matrix
    c = []
    for i in range(rows_A):
        row = []
        for j in range((cols_B)):
            row.append(0)
        c.append(row)

    # Matrix multiplication
    for i in range(rows_A):
        for j in range((cols_B)):
            for k in range(cols_A):
                c[i][j] += A[i][k] * B[k][j]
    return c