def transposeMatrix(matrix):
    transpose_matrix= []
    for col in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        transpose_matrix.append(new_row)
    return transpose_matrix
