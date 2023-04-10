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
