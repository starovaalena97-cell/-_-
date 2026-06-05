"""
Тесты для модуля widget.
"""

import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture
def card_data():
    """Фикстура с данными карт."""
    return [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ]


@pytest.fixture
def account_data():
    """Фикстура с данными счетов."""
    return [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ]


@pytest.fixture
def date_data():
    """Фикстура с данными дат."""
    return [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-25T10:30:00.000000", "25.12.2023"),
        ("2025-01-01T00:00:00", "01.01.2025"),
    ]


def test_mask_account_card_visa():
    """Тест маскировки карты Visa."""
    result = mask_account_card("Visa Platinum 7000792289606361")
    assert result == "Visa Platinum 7000 79** **** 6361"


def test_mask_account_card_maestro():
    """Тест маскировки карты Maestro."""
    result = mask_account_card("Maestro 1596837868705199")
    assert result == "Maestro 1596 83** **** 5199"


def test_mask_account_card_mastercard():
    """Тест маскировки карты MasterCard."""
    result = mask_account_card("MasterCard 7158300734726758")
    assert result == "MasterCard 7158 30** **** 6758"


def test_mask_account_card_account():
    """Тест маскировки счета."""
    result = mask_account_card("Счет 73654108430135874305")
    assert result == "Счет **4305"


def test_mask_account_card_account_another():
    """Тест маскировки другого счета."""
    result = mask_account_card("Счет 64686473678894779589")
    assert result == "Счет **9589"


def test_mask_account_card_cards(card_data):
    """Тест маскировки карт с фикстурой."""
    for input_data, expected in card_data:
        assert mask_account_card(input_data) == expected


def test_mask_account_card_accounts(account_data):
    """Тест маскировки счетов с фикстурой."""
    for input_data, expected in account_data:
        assert mask_account_card(input_data) == expected


def test_mask_account_card_invalid():
    """Тест некорректного ввода."""
    assert mask_account_card("") == ""
    assert mask_account_card("Visa") == "Visa"
    assert mask_account_card("Счет") == "Счет"


def test_get_date():
    """Тест преобразования даты."""
    result = get_date("2024-03-11T02:26:18.671407")
    assert result == "11.03.2024"


def test_get_date_another():
    """Тест преобразования другой даты."""
    result = get_date("2023-12-25T10:30:00.000000")
    assert result == "25.12.2023"


def test_get_date_with_fixture(date_data):
    """Тест преобразования даты с фикстурой."""
    for date_string, expected in date_data:
        assert get_date(date_string) == expected


def test_get_date_invalid():
    """Тест некорректной даты."""
    assert get_date("") == ""
    assert get_date("not a date") == "not a date"
