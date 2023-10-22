import copy

class Address:
    def __init__(self, street_address, city, country) -> None:
        self.city = city
        self.street_address = street_address
        self.country = country
    
    def __str__(self) -> str:
        return f"{self.street_address}, {self.city}, {self.country}"


class Person:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
    
    def __str__(self) -> str:
        return f"{self.name} lives at {self.address}"

##### None
# john = Person('John', Address("123 London Road", "London", "UK"))
# print(john)
# jane = john
# jane.name = 'jane'
# print("---")
# print(john)
# print(jane)

##### None
# address = Address("123 London Road", "London", "UK")
# john = Person('John', address)
# print(john)
# jane = Person('Jane', address)
# print("---")
# jane.address.street_address = "123B London Road"
# print(john)
# print(jane)

#### YEEES Решает проблему копирования
john = Person('John', Address("123 London Road", "London", "UK"))
jane = copy.deepcopy(john)
#jane = copy.copy(john) # Плохо это поверхностная копия только внешн класс
jane.name = 'jane'
jane.address.street_address = "124 London Road"
print("---")
print(john)
print(jane)