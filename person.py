class Person:
    def __init__(self, name):
        self.__name = name
        self.__age = 0

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")

    def __str__(self):
        return f"Имя: {self.__name}, Возраст: {self.__age}";
'''
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age in range(1,100):
            self.__age = age
        else:
            print("Недопустимый возраст")
'''



