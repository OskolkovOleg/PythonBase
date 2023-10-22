# finaly else

try:
    x, y = map(int, input().split())
    res = x/y
except ZeroDivisionError as z:
    print(z)
except ValueError as z:
    print(z)
else:
    print("Исключений не произошло")
finally:
    print("Блок finally выполняется всегда")


# Зачем finally:
try:
    f = open("myfile.txt")
    f.write("hello")
except FileNotFoundError as z:
    print(z)
except:
    print("Другая ошибка")
finally:
    f.close() # Файл нужно закрывать всегда но лучше with
    print("Файл закрыт")


def get_values():
    try:
        x, y = map(int, input().split())
        return x, y
    except ValueError as z:
        print(z)
    except:
        print("Другая ошибка")
    finally:
        print("Finally выполнился до return")
    
x, y = get_values()
print(x, y)


try:
    x, y = map(int, input().split())
    try:
        res = x/y
    except ZeroDivisionError as z:
        print(z)
except ValueError as z:
    print(z)
