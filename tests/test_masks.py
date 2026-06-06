"""
Тесты для модуля masks.
"""

import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тесты для get_mask_card_number с параметризацией
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("0000000000000000", "0000 00** **** 0000"),
        ("9999999999999999", "9999 99** **** 9999"),
    ],
)
def test_get_mask_card_number_parametrized(card_number, expected):
    """Параметризованный тест маскировки карты."""
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_with_fixture(valid_card_numbers):
    """Тест маскировки карты с использованием фикстуры."""
    for card_number, expected in valid_card_numbers:
        assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_invalid(invalid_card_numbers):
    """Тест маскировки невалидных номеров карт."""
    for card_number, expected in invalid_card_numbers:
        assert get_mask_card_number(card_number) == expected


# Тесты для get_mask_account с параметризацией
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("1234567890", "**7890"),
        ("0000", "**0000"),
        ("12345678901234567890", "**7890"),
    ],
)
def test_get_mask_account_parametrized(account_number, expected):
    """Параметризованный тест маскировки счета."""
    assert get_mask_account(account_number) == expected


def test_get_mask_account_invalid(invalid_account_numbers):
    """Тест маскировки невалидных номеров счетов."""
    for account_number, expected in invalid_account_numbers:
        assert get_mask_account(account_number) == expected


def test_get_mask_account_short():
    """Тест короткого номера счета."""
    assert get_mask_account("123") == "123"
    assert get_mask_account("") == ""
