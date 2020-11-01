from random import randint


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        matrix_tmp = ""
        for row in self.matrix:
            matrix_tmp += "\t\t".join(map(str, row)) + "\n"
        return matrix_tmp

    def __add__(self, other):
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[i]))]
                       for i in range(len(self.matrix))])


matrix_1 = [[randint(0, 100) for _ in range(3)] for _ in range(3)]
matrix_2 = [[randint(0, 100) for _ in range(3)] for _ in range(3)]

m_1 = Matrix(matrix_1)
m_2 = Matrix(matrix_2)

print(m_1 + m_2)
