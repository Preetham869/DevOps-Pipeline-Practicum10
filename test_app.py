import pytest

from app import calculate_discount, validate_username


def test_high_discount():
    assert calculate_discount(1500) == 150


def test_medium_discount():
    assert calculate_discount(750) == 37.5


def test_no_discount():
    assert calculate_discount(300) == 0


def test_negative_amount():
    with pytest.raises(ValueError):
        calculate_discount(-100)


def test_valid_username():
    assert validate_username("admin") is True


def test_empty_username():
    assert validate_username("") is False