from src.item import Item
import pytest

@pytest.fixture
def test_item():
    return Item("Смартфон", 10000, 20)

def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.pay_rate == 0.8
    assert item1.price == 8000

def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert Item.all[-2].name == 'Мышка'

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5

def test_repr(test_item):
    assert repr(test_item) == "Item('Смартфон', 10000, 20)"

def test_str(test_item):
    assert str(test_item) == 'Смартфон'

def test_item_add(test_item):
    assert test_item + test_item == 40
