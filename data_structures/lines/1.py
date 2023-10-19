# Проверка на анограмность
from collections import Counter


print(Counter("test") == Counter("tets"))
print(Counter("teset") == Counter("tets"))