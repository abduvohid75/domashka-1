from src.item import Item

class MixinLanguage:
    __slots__ = ["EN", "RU"]
    language ="EN"
    def change_lang(self):
        if  not isinstance(self.language, str) or self.language == "CH":
            raise ValueError('AttributeError: property language of KeyBoard object has no setter')

        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"
        return self
class KeyBoard(Item, MixinLanguage):
    def __int__(self, item_name, price, quantity, language = "EN"):
        super().__int__(item_name, price, quantity)
        self.language = language

class Phone(KeyBoard):
    pass

