# print(x := 1)
# # print(x=1) не роб
# a = (b := 1)
# print(a)
# print(b)


# def test():
#     return 5


# if x := test():
#     print(x)    # Не нужно повторно вызывать функцию


# while (value := input("Name ")) != "":  # Справа выполниться первое
#     print(value)


# def test(num):
#     return num * 2


# data = [1, 2, 3, 4]
# f_data = [y for x in data if (y := test(x)) != 4]
# f_data = [test(x) for x in data if test(x) != 4]  # А если функция выполняется час? год? в два раза дольше
# print(f_data)


# lines = ["#11", "22", "33"]

# if any((comment := line).startswith('#') for line in lines):
#     print(comment)


# print(num := 1, file=open('1.txt', 'w'))
