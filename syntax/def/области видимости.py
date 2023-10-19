# N = 100

def my_func(lst):
    global N # Не создаем новую переменную в локалке а Глобально
    N = 20
    for x in lst:
        n = x + 1 + N
        print(n)
    

my_func([1, 2, 3])
print(N)


x = 0
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print("inner: ", x)
    
    inner()
    print("outer: ", x)
    
outer()
print("global: ", x)