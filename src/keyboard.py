from src.item import Item


class MixinKeyLang:
    """Миксин для ввода раскладки"""
    __slots__ = ('__language')

    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        """Сеттер"""
        raise AttributeError("property 'language' of 'KeyBoard' object has no setter.")

    def change_lang(self):
        """Смена раскладки"""
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"
        return self


class Keyboard(Item, MixinKeyLang):
    """реализация класса KeyBoard"""

    def __init__(self, *args):
        super().__init__(*args)
