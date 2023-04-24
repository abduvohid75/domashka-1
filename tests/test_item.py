"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
Item.pay_rate = 0.8

def test_calculate_total_price():
    assert item1.price * item1.quantity == 200000
    assert item2.price * item2.quantity == 100000

def test_apply_discount():
    assert  item1.price * Item.pay_rate == 8000
    assert  item2.price * Item.pay_rate == 16000
