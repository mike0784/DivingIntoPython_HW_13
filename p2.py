from ExeptionMatrix import sizeMatrixException, collsRowsMatrixExeption
class matrix:
    """Класс работы с матрицами__doc__"""
    def __init__(self, mat: list) -> None:
        """Создание класса"""
        self.m = mat
        self.rows = len(mat)
        self.colls = len(mat[0])
    
    def getPrint(self) -> None:
        """Функция печати матрицы"""
        for i in range(0, self.rows):
            for j in range(0, self.colls):
                print(str(self.m[i][j]) + " ", end=" ")
            print()
    
    def __eq__(self, __value: "matrix") -> bool:
        """Функция сравнения двух матриц"""
        if len(self.m) == len(__value.m):
            for i in range(0, len(self.m)):
                for j in range(0, len(self.m[i])):
                    if self.m[i][j] != __value.m[i][j]:
                        return False
            return True
        else:
            print("Размеры матриц не совпадают")
            return False
    
    def __add__(self, __value: "matrix"):
        """Функция сложения двух матриц"""
        result = []
        if self.rows == __value.rows and self.colls == __value.colls:
            for i in range(0, self.rows):
                temp = []
                for j in range(0, self.colls):
                    a = self.m[i][j] + __value.m[i][j]
                    temp.append(a)
                result.append(temp)
            return matrix(result)
        else:
            raise sizeMatrixException()
            return None

    def __mul__(self, __value: "matrix"):
        """Функция умножения двух матриц"""
        if self.colls == __value.rows:
            result = [[0 for x in range(self.colls)] for y in range(self.rows)]
            for i in range(0, self.rows):
                for j in range(0, self.colls):
                    for k in range(0, __value.rows):
                        result[i][j] += self.m[i][k] * __value.m[k][j]
            return matrix(result)
        else:
            raise collsRowsMatrixExeption(self.colls, __value.rows)
            return None

if __name__ == "__main__":
    m1 = [
        [1, 3, 6],
        [4, 6, 2],
        [2, 9, 7]
    ]

    m2 = [
        [1, 3, 6],
        [4, 6, 2],
        [2, 9, 7],
        [3, 4, 8]
    ]
    obj1 = matrix(m1)
    

    obj2 = matrix(m2)
    obj1.getPrint()
    print()
    obj2.getPrint()

    print(f'сравнение матриц {obj1 == obj2}')

    #obj3 = obj1 + obj2
    #obj3.getPrint()
    #print()
    obj4 = obj1 * obj2
    obj4.getPrint()

    print(f"Документация класса: {matrix.__doc__ = }")
    print(f"Документация метода getPrint: {obj1.getPrint.__doc__}")
    print(f"Документация метода __eq__: {obj1.__eq__.__doc__}") 