class Dogs:
    def __init__(self, name, age, color):
        self.__name = name
        self.__age = age
        self.__color = color

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_color(self):
        return self.__color

    def set_age(self, age):
        self.__age = age

    def bark(self):
        print(f"Собака {self.get_name()}, возраст: {self.get_age()}, цвета {self.get_color()} гавкает громко")



