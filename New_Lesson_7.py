#  -------------------------------------------------------- 1 ----------------------------------------------------------


class Matrix:
    def __init__(self, args):
        self.args = args

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.args]))

    def __add__(self, other):
        result = []
        num = []
        if len(self.args) == len(other.args):
            for i in range(len(self.args)):
                for j in range(len(self.args[i])):
                    num.append(self.args[i][j] + other.args[i][j])
                    if len(num) == len(self.args[i]):
                        result.append(num)
                        num = []
        else:
            print("Matrix must be the same size")
        return result


m_new_1 = Matrix([[1, 2], [3, 4], [5, 6]])
m_new_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(m_new_1)
print(m_new_1 + m_new_2)

#  ------------------------------------------- вариант решения ---------------------------------------------------------

a = [[5, 3, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]]
b = [[1, 1, 1, 2], [2, 2, 2, 2], [3, 3, 3, 1]]


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, c))


matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(f"Matrix 1\n{matrix_1}\n{'-'*20}")
print(f"Matrix 2\n{matrix_2}\n{'-'*20}")
print(f"matrix 1 + matrix 2\n{matrix_1 + matrix_2}")

#  ------------------------------------------- вариант решения ---------------------------------------------------------


class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        return Matrix([self.matrix[i][j] + other.matrix[i][j] for i in range(len(self.matrix))]
                      for j in range(len(self.matrix[0])))


stroki = int(input("Введите количество строк и столбцов матрицы: "))
stolbci = stroki

matrix1 = Matrix([[i * j for j in range(stroki)] for i in range(stolbci)])
matrix2 = Matrix([[i + j for j in range(stroki)] for i in range(stolbci)])

print('First matrix:\n', matrix1, end='\n\n')
print('Second matrix:\n', matrix2, end='\n\n')
print('Summ of first and second matrix:\n', matrix1 + matrix2)

#  -------------------------------------------------------- 2 ----------------------------------------------------------


from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, param):
        super().__init__(param)

    @property
    def consumption(self):
        return f"Consumption of fabric for sewing a coat - {round(self.param / 6.5) + 0.5}"

class Costume(Clothes):
    def __init__(self, param):
        super().__init__(param)

    @property
    def consumption(self):
        return f"Consumption of fabric for sewing a costume - {2 * self.param + 0.3}"

coat = Coat(42)
costume = Costume(170)
print(coat.consumption)
print(costume.consumption)

#  ------------------------------------------- вариант решения ---------------------------------------------------------

#  -------------------------------------------------------- 3 ----------------------------------------------------------


class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return self.nums

    def __add__(self, other):
        return f'Sum of cell is: {self.nums + other.nums}'

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else "Ячеек в первой клетке меньше равно второй, вычитание невозможно!"

    def __mul__(self, other):
        return f'Multiply of cells is: {self.nums * other.nums}'

    def __truediv__(self, other):
        return f'Truediv of cells is: {round(self.nums / other.nums)}'


cell_1 = Cell(15)
cell_2 = Cell(24)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_2.make_order(7))