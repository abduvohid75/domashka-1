import csv
import json
import os

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.general_summ = self.price * self.quantity
        self.all.append(self)

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            print('Длина товара превышает 10 символов')
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f"{self.__name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """

        return self.price * self.quantity

    def __add__(self, other):
        if not isinstance(other, Phone):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return int(self.quantity) + int(other.quantity)

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
    @classmethod
    def instantiate_from_csv(cls):
        path = os.path.join(os.path.dirname(__file__), "items.csv")
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            cls.all.clear()
            for row in reader:
                print(row)
                cls.all.append(cls(row['name'], int(row['price']), int(row['quantity'])))

        return len(cls.all)

    @staticmethod
    def string_to_number(number):
        return int(float(number))

