from dataclasses import dataclass, asdict

# Чтобы использовать определенные типы


@dataclass
class User:
    name: str
    age: int

    # Лучше без методов Как бы класс данных
    def get_name(self) -> None:
        print(self.name)


# a = User("1", 1)
# a.get_name()

class UserHandle:
    def __init__(self, name, age) -> None:
        self.user = User(name, age)

    def get_dataclass(self):
        return asdict(self.user)

    def edit(self, key, value):
        self.user.__dict__[key] = value


def test(user: User):
    pass

p = UserHandle("1", 1)
print(p.user.age)
print(p.get_dataclass())