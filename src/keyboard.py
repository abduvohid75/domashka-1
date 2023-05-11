from src.item import Item

class MixinLanguage:
    __slots__ = ["EN", "RU"]
    language ="EN"
    def change_lang(self):

        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"
        else:
            raise AttributeError('property language of KeyBoard object has no setter')
        return self
class KeyBoard(Item, MixinLanguage):
    def __int__(self, item_name, price, quantity, language = "EN"):
        super().__int__(item_name, price, quantity)
        self.language = language

class Phone(KeyBoard):
    pass


