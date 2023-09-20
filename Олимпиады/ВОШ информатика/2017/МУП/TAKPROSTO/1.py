# open('Otvet.txt', 'w') # Перезапись
# open('Otvet.txt', 'a') # Дозапись
# open('Otvet.txt', 'r') # Чтение

7
a = "2,3,7,21,5,6"
b = [2,3,4,45,6,76]

2
3
4
45
6
76

c = [23,23,23,23,54,6,6,65,43]
d = ['OPOOPOPOPOPOPIOPIPIPODBDHNHRF']
e = ['p','о','с','с','и','я']

with open('Otvet.txt', 'w', encoding='UTF-8') as file:
    for i in c:
        file.write(f'{i},')   

