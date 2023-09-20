# from module import Bytes


# class Locker:
#     ...


# def get_value():
#     value: Bytes = 0x1


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from module import Bytes


class Locker:
    ...


def get_value():
    value: Bytes = 0x1