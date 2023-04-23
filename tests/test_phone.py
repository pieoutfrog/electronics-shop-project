import pytest

from src.item import Item
from src.phone import Phone


class New:
    """Класс не связанный с Item, для теста add"""

    def __init__(self, name: str, price: float, quantity: int, sim_cards_num: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.sim_cards_num = sim_cards_num


@pytest.fixture
def return_date():
    """Описание фикстуры для тестов"""
    return Phone("Смартфон", 70000, 10, 1)


def test_init(return_date):
    """Тест для init"""
    assert return_date.price == 70000
    assert return_date.name == 'Смартфон'
    assert return_date.quantity == 10
    assert return_date.sim_cards_num == 1


def test_number_of_sim():
    """Тест переменой количества симок"""
    date = Phone("Смартфон", 70000, 10, 2)
    assert date.sim_cards_num == 2
    with pytest.raises(ValueError):
        date.sim_cards_num = 0


def test_repr(return_date):
    """Тест для метода repr"""
    assert repr(return_date) == "Phone('Смартфон', 70000, 10, 1)"


def test_add():
    """Тест для метода сложения количества товара двух экземпляров"""
    phone1 = Phone("Sumsung_ZIP", 100000, 15, 2)
    item1 = Item("Смартфон", 70000, 10)
    phone2 = New("Sumsung_ZIP", 100000, 15, 2)
    assert phone1 + item1 == 25
    assert phone1 + phone1 == 30
    assert item1 + item1 == 20
    with pytest.raises(Exception):
        phone1 + phone2