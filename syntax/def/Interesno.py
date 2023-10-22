# Вот так не надо
def f(lst=[]):
    lst.append(2)
    return lst

# Надо вот так:
def f(lst=None):
    if lst is None:
        lst = []
        
    lst.append(2)
    return lst