# 3031varun
class Matrix:
    def __get_dimensions(self, m_1, m_2=None):
        rows_1 = len(m_1)
        cols_1 = len(m_1[0])
        dim_1 = (rows_1, cols_1)
        if m_2 is not None:
            rows_2 = len(m_2)
            cols_2 = len(m_2[0])
            dim_2 = (rows_2, cols_2)
            same_dim = dim_1 == dim_2
            comp_dim = cols_1 == rows_2
            return dim_1, dim_2, same_dim, comp_dim
        else:
            return dim_1

    def addition(self, m_1, m_2):
        dim_1, dim_2, same_dim, comp_dim = self.__get_dimensions(m_1, m_2)
        if not same_dim:
            raise Exception("Matrices do not have the same dimensions")
        sum_m = [[0 for cols in range(dim_1[1])] for rows in range(dim_1[0])]
        for i in range(0, dim_1[0]):
            for j in range(0, dim_1[1]):
                sum_m[i][j] = m_1[i][j] + m_2[i][j]
        return sum_m

    def multiplication(self, m_1, m_2):
        dim_1, dim_2, same_dim, comp_dim = self.__get_dimensions(m_1, m_2)
        if not comp_dim:
            raise Exception("Matrices do not have compatible dimensions")
        product_m = [[0 for cols in range(dim_2[1])] for rows in range(dim_1[0])]
        for i in range(0, dim_1[0]):
            for j in range(0, dim_2[1]):
                for k in range(0, dim_2[0]):
                    product_m[i][j] += m_1[i][k] * m_2[k][j]
        return product_m

    def transpose(self, m):
        dim = self.__get_dimensions(m)
        transpose_m = [[0 for cols in range(dim[0])] for rows in range(dim[1])]
        for i in range(0, dim[0]):
            for j in range(0, dim[1]):
                transpose_m[j][i] = m[i][j]
        return transpose_m

    def display(self, m):
        for row in m:
            print(row)


if __name__ == '__main__':
    matrix_1 = [[10, 20, 30], [40, 5, 6], [7, 8, 9]]
    matrix_2 = [[10, 20, 30], [40, 5, 6], [7, 8, 9]]
    matrix_3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_4 = [[1, 2], [4, 5], [7, 8]]

    matrix = Matrix()
    sum = matrix.addition(matrix_1, matrix_2)
    transpose = matrix.transpose(matrix_3)
    product = matrix.multiplication(matrix_3, matrix_4)
    print('Matrix 1:')
    matrix.display(matrix_1)
    print('Matrix 2:')
    matrix.display(matrix_2)
    print('Matrix 3:')
    matrix.display(matrix_3)
    print('Matrix 4:')
    matrix.display(matrix_4)
    print('Transpose of Matrix 3:')
    matrix.display(transpose)
    print('Addition of Matrix 1 & 2:')
    matrix.display(sum)
    print('Multiplication of Matrix 3 & 4:')
    matrix.display(product)
