# class Goods:
#     def __init__(self, name, weight, price) -> None:
#         super().__init__()
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price

#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")


# class MixingLog:
#     ID = 0

#     def __init__(self) -> None:
#         print("Init MixinLog")
#         self.ID += 1
#         self.id = self.ID

#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов")


# # Сам посебе выполниться лишь один init
# class NoteBook(Goods, MixingLog):  # Порядок имеет значение
#     pass


# n = NoteBook('Acer', 1.5, 30_000)
# n.print_info()
# n.save_sell_log()
# print(NoteBook.__mro__)


