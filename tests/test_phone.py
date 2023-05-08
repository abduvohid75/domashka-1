import pytest
from src.item import Item
from src.phone import Phone

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
phone1 = Phone("iPhone 14", 120000, 5, 2)

def test_add():
    assert item1 + phone1 == 25

def test_init():
    assert phone1.number_of_sim == 2