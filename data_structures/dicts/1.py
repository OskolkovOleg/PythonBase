# d = {'a': 1, 'b': 2}

# print(d.get('c'))
# print(d.get('c', 3)) # Значение по умолчанию


import base64
import webbrowser


class OverloadDict(dict):
    def __missing__(self, key):
        image = ''
        result = base64.b64decode(image).decode("utf-8")
        webbrowser.open(url=result)
        return key


example = OverloadDict(name="Alex", age=17)
print(example)
print(example["root"])