try:
    f = open("myfile.txt")
except FileNotFoundError:
    print("Невозномно открыть файл")



try:
    x, y = map(int, input().split())
    res = x / y
except ValueError:
    print("Ошибка типа данных")
except ZeroDivisionError:
    print("Ltktybt yf yjkm")

except (ZeroDivisionError, ValueError):
    print("Ош")
except:
    print("Ошибка")
 
print("Штатное завершение")
