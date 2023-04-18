import pytest
from src.item import Item


@pytest.fixture()
def item1():
    return Item('Laptop', 50000, 2)


def test_item_calculate_total_price(item1):
    assert item1.calculate_total_price() == 100000


def test_item_apply_discount(item1):
    item1.apply_discount()
    assert item1.price == 42500


def test_string_to_number():
    """тест для статик метода, переводящего число-строку в число"""
    assert Item.string_to_number("8") == 8


def test_name():
    """тест для сеттера name """
    item = Item("Стиралка", 40000, 50)
    item.name = "Стиралка"
    assert item.name == "Стиралка"
    item1 = Item("Холодильник", 80000, 10)
    item1.name = "Холодильник"
    assert item1.name == "Холодильник"


def test_instantiate_from_csv():
    """Тест для класс.метода открытия csv-файла"""
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Вентилятор'
    assert item1.price == 100
    assert item1.quantity == 1

    item2 = Item.all[1]
    assert item2.name == 'Телевизор'
    assert item2.price == 1000
    assert item2.quantity == 3


def test_str(item1):
    """Тест для метода str"""
    assert str(item1) == 'Laptop'


def test_repr(item1):
    """Тест для метода repr"""
    assert repr(item1) == "Item('Laptop', 50000, 2)"
