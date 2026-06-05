"""
Модуль для работы с виджетами банковских операций.
"""

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_info: str) -> str:
    """
    Маскирует номер карты или счета в строке.

    Принимает строку с типом и номером карты/счета,
    возвращает строку с замаскированным номером.

    Args:
        card_or_account_info: Строка вида "Visa Platinum 7000792289606361"
                              или "Счет 73654108430135874305"

    Returns:
        Строка с замаскированным номером

    Example:
        >>> mask_account_card("Visa Platinum 7000792289606361")
        'Visa Platinum 7000 79** **** 6361'
        >>> mask_account_card("Счет 73654108430135874305")
        'Счет **4305'
    """
    # Защита от некорректного ввода
    if not card_or_account_info or len(card_or_account_info.split()) < 2:
        return card_or_account_info

    # Разделяем на тип и номер
    parts = card_or_account_info.rsplit(" ", 1)
    card_type = parts[0]
    number = parts[1]

    # Определяем, карта это или счет
    if card_type.lower() == "счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{card_type} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует дату из ISO формата в формат ДД.ММ.ГГГГ.

    Args:
        date_string: Строка с датой в формате "2024-03-11T02:26:18.671407"

    Returns:
        Строка с датой в формате "11.03.2024"

    Example:
        >>> get_date("2024-03-11T02:26:18.671407")
        '11.03.2024'
    """
    from datetime import datetime

    # Защита от некорректного ввода
    if not date_string:
        return ""

    try:
        # Парсим ISO формат
        date_obj = datetime.fromisoformat(date_string)
        # Возвращаем в формате ДД.ММ.ГГГГ
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return date_string