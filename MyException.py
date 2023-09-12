class myException(Exception):
    pass

class titleException(myException):
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return f'Вводимое вами фамилия, имя или отчество должно начинаться с заглавной буквы\nВы ввели: {self.value}'
    
class alphaException(myException):
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return f'В введеной вами фамилии, имени или отчестве имеются недопустимые символы {self.value}\nДолжны быть только буквы'