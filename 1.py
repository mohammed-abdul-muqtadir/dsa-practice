def setZeroes(mat):
    row = []
    col = []
    # no of row
    for i in range(len(mat)):
        # no of col
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                row.append(i)
                col.append(j)
    # making row as zero
    for i in row:
        mat[i] = [0] * len(mat[0])
    # making col as zero
    for j in col:
        for i in range(len(mat)):
            mat[i][j] = 0
    print(mat)


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

setZeroes(matrix)
