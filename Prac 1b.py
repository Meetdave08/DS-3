matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum_matrix = [[None, None, None], [None, None, None], [None, None, None]]
for i in range(0, 3):
    for j in range(0, 3):
        sum_matrix[i][j] = matrix[i][j] + matrix_2[i][j]
print(sum_matrix)
