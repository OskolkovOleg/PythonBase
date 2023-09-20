# Реализует независимое пространство имен
class Women:
    title = "объект класса для поля title"
    photo = "объект класса для поля photo"
    ordering = "объект класса для поля ordering"

    def __init__(self, user, psw) -> None:
        self._user = user
        self._psw = psw
        self.meta = self.Meta(1)


    class Meta:
        ordering = ["id"]

        def __init__(self, access) -> None:
            self._access = access
            self._t = Women.title # Так делать точно не надо!!!



w = Women("root", "12345") # Не создается объект класса Meta
print(w.ordering)
print(w.Meta.ordering)
print(w.__dict__)
print(w.meta.__dict__)