"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
phone1 = Phone("iPhone 14", 120000, 5, 2)
Item.pay_rate = 0.8

def test_calculate_total_price():
    assert item1.price * item1.quantity == 200000
    assert item2.price * item2.quantity == 100000

def test_apply_discount():
    assert  item1.price * Item.pay_rate == 8000
    assert  item2.price * Item.pay_rate == 16000

def test_repr():
  #  assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert int(repr(item1.quantity)) + int(repr(phone1.quantity)) == 25
    assert phone1.quantity + phone1.quantity == 10


def test_str():
    assert str(item1) == 'Смартфон'

def test_add():
    assert item1 + phone1 == 25



