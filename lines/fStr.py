import datetime
name = "Alex"
val = 17
print(f"{name}, {val}")
print(f"{name=}")

print(f"{20.1: .5f}")

now = datetime.datetime
print(f"{now.utcnow()=:'%d:%m:%y'}")

data = [("x", "y", "sum"), (1, 2, 3), (3, 5, 8)]
for x, y, sum in data:
    # Количество пробелов занимаемое
    print(f"{x:1} {y:1} {sum:2}")
