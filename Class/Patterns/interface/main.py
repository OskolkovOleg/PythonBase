# Интерфейс это абстрактный класс 
# вкотором все методы надо переопределять
# Он не содержит никаких данных
# Ничего нового
from abc import ABC
from abc import abstractmethod

class A(ABC):
    @abstractmethod
    def get() -> None:
        print("A")

class B:
    def get() -> None:
        print("B")

class C(A, B):
    def __init__(self) -> None:
        pass

c = C()
c.get()