"""
Тесты для модуля masks.
"""

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    """Тестирует маскировку номера карты."""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_card_number_invalid_length():
    """Тестирует номер карты неправильной длины."""
    assert get_mask_card_number("1234") == "1234"


def test_get_mask_card_number_with_letters():
    """Тестирует номер карты с буквами."""
    assert get_mask_card_number("700079228960636a") == "700079228960636a"


def test_get_mask_account():
    """Тестирует маскировку номера счета."""
    assert get_mask_account("73654108430135874305") == "**4305"


def test_get_mask_account_short():
    """Тестирует короткий номер счета."""
    assert get_mask_account("123") == "123"


def test_get_mask_account_four_digits():
    """Тестирует номер счета из 4 цифр."""
    assert get_mask_account("1234") == "**1234"
