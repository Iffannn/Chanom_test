import pytest
from calculate_price import calculate_price
def test_calculate_price_with_no_toppings():
    assert calculate_price([]) == 25

def test_calculate_price_with_one_topping():
    assert calculate_price(["ไข่มุก"]) == 30

def test_calculate_price_with_two_toppings():
    assert calculate_price(["เฉาก๊วย", "วิปครีม"]) == 50

def test_calculate_price_with_more_than_two_toppings():
    with pytest.raises(ValueError):
        calculate_price(["ไข่มุก", "เฉาก๊วย", "ถั่วแดง"])

def test_calculate_price_with_duplicate_toppings():
    with pytest.raises(ValueError):
        calculate_price(["ไข่มุก", "เฉาก๊วย", "ไข่มุก"])