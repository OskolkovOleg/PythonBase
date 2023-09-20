# from test import test_func


# def test2_func():
#     print(f"name: {__name__}")
# ^Цикл импорта так нельзя^


# А это впринципе работает Но лучше просто так так не делать
def test2_func():
    from test import test_func
    print(f"name: {__name__}")


import test # Нельзя называть модули названиями используемых библиотек 

def test2_func():
    print(f"name: {__name__}")
# ^Цикл импорта так нельзя^
