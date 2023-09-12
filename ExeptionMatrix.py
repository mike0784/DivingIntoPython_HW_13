class sizeMatrixException(Exception):
    def __str__(self) -> str:
        return f'Размер матрицы А должен совпадать с размером матрицы B'

class collsRowsMatrixExeption(Exception):
    def __init__(self, value1: int, value2: int) -> None:
        self.value1 = value1
        self.value2 = value2
    
    def __str__(self) -> str:
        return f'Количество столбцов матрицы A {self.value1} должен совпадать с количеством строк матрицы B {self.value2}'