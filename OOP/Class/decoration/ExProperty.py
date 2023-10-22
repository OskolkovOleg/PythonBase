from string import ascii_letters

class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфчцчшщъыьэюя-'
    S_RUS_UPPER = S_RUS.upper()
    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.__fio = fio.split()
        self.__old = old              #Через сеттер
        self.passport = ps
        self._weight = weight 
    

    @classmethod
    def verify_fio(cls, fio: str) -> None:
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой!')
        
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный параметр записи")
        
        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("В ФИО должен быть хотя бы один символ")
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО можно использовать только буквенные символы и девис")
    
    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError('Возраст должно быть целым числом в диапозоне [14; 120]')
        
    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError('Возраст должен быть вещественным числом от 20 и выше')

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError('Паспорт должен быть строкой')

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный формат паспорта")

        for p in s:
            if not p.isdigit():
                raise TypeError("Серия и номер паспорта должны быть числами")


    @property  
    def fio(self):
        return self.__fio
    
    @property  
    def old(self):
        return self.__old
    
    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    
    @property  
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    
    @property  
    def passport(self):
        return self.__passport
    
    @passport.setter
    def passport(self, passport):
        self.verify_ps(passport)
        self.__passport = passport
        

p = Person('Осколков Олег Сергеевич', 15, '1234 567890', 80.0)
p.old = 100
p.old = 30
print(p.old)