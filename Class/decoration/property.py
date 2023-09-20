class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    # Приоритет у объекта property выше чем у других локальных объектов
    old = property(get_old, set_old) # Но так дублирование интерфейсов
    # Можно:
    old  = property()
    old = old.setter(set_old)
    old = old.getter(get_old)

    # А так супер ок нет функционального дублирования
    @property  # Обязательно перед геттером
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old


p = Person('Олег', 15)
p.old = 35
del p.old
print(p.__dict__)
