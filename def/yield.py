def test():
    for i in range(3):
        yield i

a = test()
print(next(a))
print(next(a))
print(next(a))

def test():   
    yield from [1, 2, 3]

def test():   
    yield from [x for x in range(20)]

def test():
    print("Started")
    while True:
        yield 1
        yield 2


def test():
    print("Started")

    while True:
        x = yield
        print("recv", x)

a = test()
next(a)
a.send("test")

# for i in test():
#     print(i)