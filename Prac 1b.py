# 3031varun
class Matrix:
    def __init__(self, m_1):
        self.m_1 = m_1

    def addition(self, m_2):
        sum_m = [[None, None, None], [None, None, None], [None, None, None]]
        for i in range(0, 3):
            for j in range(0, 3):
                sum_m[i][j] = self.m_1[i][j] + m_2[i][j]
        return sum_m


if __name__ == '__main__':
    matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = Matrix(matrix_1)
    print(matrix.addition(matrix_2))
