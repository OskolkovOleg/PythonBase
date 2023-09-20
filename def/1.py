
# 1.Понятность

def f(value): ... #Что за название Что она делает Что передавать Что вернёт


def get_array(value: int) -> list:  
    if value == 2:
        return [x for x in range(5)]
    else:
        return [x for x in range(2)]


# 2.Уникальность

def get_name():
    return "Name"


def get_name():
    return "222"


print(get_name)


# 3.Информативность
    # Много плохо:

# Возвращает имя функции
def get_name(): # Объявление функции
    return "Name" # Возвращаем строку ;)

    # Мало плохо
def proccessing(): ...
def value_hander(): ...
def message_hander(): ...

    # Лучше:
def get_name():
    return "Name"


# 3.Название осмысленно и отражает суть функции
def proccessing(): ...
def value_hander(): ...
def message_hander(): ...
    # "Это все малопонятно"


# 4. Иногда лучше класс:

def add_value(): ...

def multiply_values(): ...

def divide_values(): ...


class Nubers:
    def __init__(self, number: int | float):
        self.number = number
    
    def add_value(): ...

    def multiply_values(): ...

    def divide_values(): ...


# 5. Функция выполняет одно действие это не модуль
    # Плохо:
def handler():
    # 1. вытаскиваемзначение из json
    # 2. отправляем запросы
    # 3. отправлем результат в телеграмм
    # 4. записываем результат в log.txt
    ...

def test():
    # записываем результат в log.txt
    ...


# 6. Использование ссылочных типов

    # Плохо:
def append_score(score, scores=[]):
    scores.append(score)
    print(scores)

append_score(98) # [98]
append_score(92, [100, 95]) # [100, 95, 92]
append_score(94) # [98, 94]
append_score(94, [22, 34]) # [22, 34, 94]
append_score(22) # [98, 94, 22] 

    # Следующий пример:
def append_score(score, scores=[]):
    scores.append(score)
    print(f"scores: {scores} & id: {id(scores)}")

append_score(98) # [98] & id: 2784632780352
append_score(92, [100, 95]) # [100, 95, 92]  & id: 2784628388864
append_score(94) # [98, 94] & id: 2784632780352
append_score(94, [22, 34]) # [22, 34, 94] & id: 2784628388864
append_score(22) # [98, 94, 22] & id: 2784632780352


# 6. *args and **kwargs

    # Так не надо, задача простая Не злоупотреблять
def add_numbers(*args, **kwargs):
    if args:
        print(args[0] + args[1])
    elif kwargs:
        print(kwargs["x"] + kwargs["y"])

    
add_numbers(*[1, 2])
add_numbers(**{"x": 3, "y": 6})