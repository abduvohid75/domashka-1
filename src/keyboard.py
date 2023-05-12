from src.item import Item


class MixinLanguage:

    def __init__(self):
        self.__language = 'EN'
        __slots__ = ["EN", "RU"]

    @property
    def get_language(self):
        return self.__language

    def change_lang(self):

        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"
        else:
            raise AttributeError('property language of KeyBoard object has no setter')
        return self


class KeyBoard(Item, MixinLanguage):
    def __init__(self, item_name, price, quantity, language="EN"):
        super().__init__(item_name, price, quantity)
        self.language = language


class Phone(KeyBoard):
    pass
