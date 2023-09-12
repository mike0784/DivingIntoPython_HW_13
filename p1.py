import os
import csv
from MyException import titleException, alphaException

class Descriptor:
    def __init__(self, value: str) -> None:
        self.name = value
    def __set_name__(self, owner, name):
        self.name = name
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value: str) -> None:
        if not value.isalpha():
            raise alphaException(value)
        if not value.istitle():
            print("istitle")
            raise titleException(value)        
        
        instance.__dict__[self.name] = value

class student:
    surname = Descriptor("surname")
    name = Descriptor("name")
    patronymic = Descriptor("patronymic")
    def __init__(self, file: str, surname: str, name: str, patronymic: str) -> None:
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
    
    
    def getSurname(self) -> str:
        return self.surname
    
    def getName(self) -> str:
        return self.name
    
    def getPatronymic(self) -> str:
        return self.patronymic

if __name__ == "__main__":
    file = "grade.csv"
    snp = input("Введите ФИО: ")
    temp = snp.split(" ")
    obj = student(file, temp[0], temp[1], temp[2])
    print(obj.getSurname())
    print(obj.getName())