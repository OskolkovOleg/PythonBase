a = type("Hello", (object,), {"value":"world"}) # Создаем класс
print(a.value)


class Hello(object):
    value = "world"


a = Hello()
print(a.value)
print(Hello.value)