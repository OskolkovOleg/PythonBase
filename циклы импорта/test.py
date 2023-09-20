# from test2 import test2_func


# def test_func():
#     print(f"name: {__name__}") 
# ^Цикл импорта так нельзя^


# А это впринципе работает Но лучше просто так так не делать
def test_func():
    from test2 import test2_func
    print(f"name: {__name__}")


# Так лучше
import test2

def test_func():
    print(f"name: {__name__}")
# ^Цикл импорта так нельзя^