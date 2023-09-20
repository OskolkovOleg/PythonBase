class ThreadData:
    __shared_attrs = {
        'name': 'tread_1',
        'data': {},
        'id': 1
    }


    def __init__(self):
        self.__dict__ = self.__shared_attrs

th1 = ThreadData()
th2 = ThreadData()
print(th1.__dict__)
print(th2.__dict__)

th2.id = 3
th1.attr_new = "new_attr"
print(th1.__dict__)
print(th2.__dict__)

# Один атрибут на всех меняется у одного мен у всех

# мало применяется