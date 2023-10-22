
# JSON 100 cls, 100 intf
# XML

# JSON - str
# XML - int

class Old:
    def get(self):
        return "1234"


class New:
    def get(self):
        return 1234


class Adapter(New):
    def get(self):
        return str(super(Adapter, self).get())


def main(obj):
    print("Результат" + obj.get())


if __name__ == '__main__':
    obj = Old()
    main(obj)
    
    obj2 = Adapter()
    main(obj2)