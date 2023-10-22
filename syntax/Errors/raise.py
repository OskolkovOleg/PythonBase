class supError(ArithmeticError):
    def __str__(self) -> str:
        return "ХАХАХАХ фуууууу"

# raise supError

class ExceptionPrintSendData(Exception):
    """Класс исключений при отправке данных принтеру"""
    def __init__(self, *args: object) -> None:
        self.message = args[0] if args else None
        super().__init__(*args)
    def __str__(self) -> str:
        return f"Ошибка: {self.message}"

    


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"печать: {str(data)}" )
        
    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData("Принтер не отвечает")

    def send_to_print(self, data):
        return False


p = PrintData()
p.print("123")
try:
    p.print("123")
except ExceptionPrintSendData:
    print("Принтер не отвечает")

z = ZeroDivisionError
raise z
raise ZeroDivisionError("Деление на ноль")

