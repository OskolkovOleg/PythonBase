
# commands = [...]

# if commands == ["make"]:
#     print("make")
# elif len(commands) == 2 and commands[0] == "make":
#     print("make2")
# elif commands == ["restart"]:
#     print("restart")
# elif len(commands) >= 1 and commands[0] == "rm":
#     print("rm")


# command = ["rm", "1", "2"]

# match command:
#     case ["make"]:
#         print("make")
#     case ["make", cmd]:
#         print(f"make: {cmd}")
#     case ["restart"]:
#         print("restart")
#     case ["rm", *files]:
#         print(f"rm files: {files}")


# value = ["start", "1", "2"]

# match value:
#     case ["start"]:
#         print("Добавьте аргументы")
#     case ["start", arg]:
#         print(f"result: {arg}")
#     case ["start", *arg]:
#         print(f"results: {arg}")
#     case ["start", *_]:  # Значения без записи в переменную
#         print(f"results: {0}")
#     case ["start", _, arg]:
#         print(f"result: {arg}")
#     case ["start", _, *arg]:
#         print(f"result: {arg}")
#     case _:
#         print(f"defalt: {value}")


# args = ["start", "help"]

# match args:
#     case ["start", ("-h" | "--help" | "help") as hlp]:
#         print(f"Аргументы: {hlp}")
#     case _:
#         print(f"defalt: {args}")


# args = ["start", "alex192"]
# black_list = ["alex192", "1221", "121221"]

# match args:
#     case ["start", nickname] if nickname not in black_list:
#         print(f"Пользователь: {nickname}")
#     case _:
#         print(f"Пользователь: {args[1]} заблокирован")


# def http_status(status: int):
#     match status:
#         case 400:
#             return "Bad request"
#         case 401:
#             return "Unauthorized"
#         case 403:
#             return "Forbidden"
#         case 404:
#             return "Not found"


class switch:
    on = 1
    off = 0

status = 0

match status:
    case switch.on:
        print("Swith is on")
    case switch.off:
        print("Swith is off")
