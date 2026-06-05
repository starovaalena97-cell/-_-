"""
Тесты для модуля widget.
"""

from src.widget import get_date, mask_account_card


def test_mask_account_card_card():
    """Тестирует маскировку номера карты."""
    result = mask_account_card("Visa Platinum 7000792289606361")
    assert result == "Visa Platinum 7000 79** **** 6361"


def test_mask_account_card_maestro():
    """Тестирует маскировку карты Maestro."""
    result = mask_account_card("Maestro 1596837868705199")
    assert result == "Maestro 1596 83** **** 5199"


def test_mask_account_card_mastercard():
    """Тестирует маскировку карты MasterCard."""
    result = mask_account_card("MasterCard 7158300734726758")
    assert result == "MasterCard 7158 30** **** 6758"


def test_mask_account_card_visa_classic():
    """Тестирует маскировку карты Visa Classic."""
    result = mask_account_card("Visa Classic 6831982476737658")
    assert result == "Visa Classic 6831 98** **** 7658"


def test_mask_account_account():
    """Тестирует маскировку номера счета."""
    result = mask_account_card("Счет 73654108430135874305")
    assert result == "Счет **4305"


def test_mask_account_account_another():
    """Тестирует маскировку другого счета."""
    result = mask_account_card("Счет 64686473678894779589")
    assert result == "Счет **9589"


def test_mask_account_card_invalid_input():
    """Тестирует некорректный ввод."""
    assert mask_account_card("") == ""
    assert mask_account_card("Visa") == "Visa"


def test_get_date():
    """Тестирует преобразование даты."""
    result = get_date("2024-03-11T02:26:18.671407")
    assert result == "11.03.2024"


def test_get_date_another():
    """Тестирует преобразование другой даты."""
    result = get_date("2023-12-25T10:30:00.000000")
    assert result == "25.12.2023"


def test_get_date_invalid():
    """Тестирует некорректную дату."""
    result = get_date("")
    assert result == ""
    result = get_date("not a date")
    assert result == "not a date"
