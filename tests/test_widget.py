"""
Тесты для модуля widget.
"""

import pytest

from src.widget import get_date, mask_account_card


def test_mask_card_visa_platinum():
    """Тест маскировки Visa Platinum."""
    result = mask_account_card("Visa Platinum 7000792289606361")
    assert result == "Visa Platinum 7000 79** **** 6361"


def test_mask_card_maestro():
    """Тест маскировки Maestro."""
    result = mask_account_card("Maestro 1596837868705199")
    assert result == "Maestro 1596 83** **** 5199"


def test_mask_card_mastercard():
    """Тест маскировки MasterCard."""
    result = mask_account_card("MasterCard 7158300734726758")
    assert result == "MasterCard 7158 30** **** 6758"


def test_mask_card_classic():
    """Тест маскировки Visa Classic."""
    result = mask_account_card("Visa Classic 6831982476737658")
    assert result == "Visa Classic 6831 98** **** 7658"


def test_mask_card_gold():
    """Тест маскировки Visa Gold."""
    result = mask_account_card("Visa Gold 5999414228426353")
    assert result == "Visa Gold 5999 41** **** 6353"


def test_mask_account():
    """Тест маскировки счета."""
    result = mask_account_card("Счет 73654108430135874305")
    assert result == "Счет **4305"


def test_mask_account_another():
    """Тест маскировки другого счета."""
    result = mask_account_card("Счет 64686473678894779589")
    assert result == "Счет **9589"


def test_mask_cards_fixture(card_data):
    """Тест маскировки карт с фикстурой."""
    for inp, exp in card_data:
        assert mask_account_card(inp) == exp


def test_mask_accounts_fixture(account_data):
    """Тест маскировки счетов с фикстурой."""
    for inp, exp in account_data:
        assert mask_account_card(inp) == exp


def test_mask_invalid():
    """Тест некорректного ввода."""
    assert mask_account_card("") == ""
    assert mask_account_card("Visa") == "Visa"
    assert mask_account_card("Счет") == "Счет"


def test_get_date_normal():
    """Тест преобразования даты."""
    result = get_date("2024-03-11T02:26:18.671407")
    assert result == "11.03.2024"


def test_get_date_another():
    """Тест преобразования другой даты."""
    result = get_date("2023-12-25T10:30:00.000000")
    assert result == "25.12.2023"


def test_get_date_fixture(date_data):
    """Тест преобразования даты с фикстурой."""
    for ds, exp in date_data:
        assert get_date(ds) == exp


def test_get_date_invalid():
    """Тест некорректной даты."""
    assert get_date("") == ""
    assert get_date("not a date") == "not a date"
