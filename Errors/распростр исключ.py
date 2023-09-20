def func2():
    try:
        return 1/0
    except:
        print('func2 Ошибка')

def func1():
    try:
        return func2()
    except:
        print('func1 Ошибка')

func1()
print("Нормально все")