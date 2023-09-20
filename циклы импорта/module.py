# from module import Locker


# class Bytes:
#     ...


# def get_value():
#     value: Locker = 0x1

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from module import Locker


class Bytes:
    ...


def get_value():
    value: Locker = 0x1
