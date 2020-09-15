# 3031varun
class Matrix:
    def addition(self, m_1, m_2):
        sum_m = [[0 for x in range(3)] for y in range(3)]
        for i in range(0, 3):
            for j in range(0, 3):
                sum_m[i][j] = m_1[i][j] + m_2[i][j]
        return sum_m

    def multiplication(self, m_1, m_2):
        product_m = [[0 for x in range(3)] for y in range(3)]
        for i in range(0, 3):
            for j in range(0, 3):
                for k in range(0, 3):
                    product_m[i][j] += m_1[i][k] * m_2[k][j]
        return product_m

    def transpose(self, m):
        transpose_m = [[0 for x in range(3)] for y in range(3)]
        for i in range(0, 3):
            for j in range(0, 3):
                transpose_m[j][i] = m[i][j]
        return transpose_m

    def display(self, m):
        for row in m:
            print(row)


if __name__ == '__main__':
    matrix_1 = [[10, 20, 30], [40, 5, 6], [7, 8, 9]]
    matrix_2 = [[10, 20, 30], [40, 5, 6], [7, 8, 9]]
    matrix_3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = Matrix()
    sum = matrix.addition(matrix_1, matrix_2)
    transpose = matrix.transpose(matrix_3)
    product = matrix.multiplication(matrix_1, matrix_2)
    print('Matrix 1:')
    matrix.display(matrix_1)
    print('Matrix 2:')
    matrix.display(matrix_2)
    print('Matrix 3:')
    matrix.display(matrix_3)
    print('Transpose of Matrix 3:')
    matrix.display(transpose)
    print('Addition:')
    matrix.display(sum)
    print('Multiplication:')
    matrix.display(product)

