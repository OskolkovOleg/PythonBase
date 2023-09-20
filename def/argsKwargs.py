# **kwargs коллекция из именнованных аргументов в виде словаря
# *args коллекция из обычных аргументов в виде кортежа

def test(*args):
    print(args)

a = [1, 2, 4]
test(*a)
test(a)

def test(*args, **kwargs):
    print(args, "\n", kwargs)

a = {"1":"1"}
test(1, *a)



def os_path(disk, *args, sep="\\", **kwargs):
    # print(args)
    # print(kwargs)
    args = (disk, ) + args
    if "trim" in kwargs and kwargs["trim"]:
        args = [x.strip() for x in args]
    
    return sep.join(args)

p = os_path("D:", "Oleg.cor", "   test.py    ", sep="/", trim=True)
print(p)