"""
Модуль generators содержит функции-генераторы для работы с транзакциями.
"""

from typing import Any, Dict, Iterator, List, Generator


def filter_by_currency(
    transactions: List[Dict[str, Any]], currency: str
) -> Iterator[Dict[str, Any]]:
    """
    Фильтрует транзакции по валюте. Возвращает итератор.

    Args:
        transactions: Список словарей с транзакциями
        currency: Код валюты (например, "USD", "RUB")

    Yields:
        Транзакции с указанной валютой
    """
    for transaction in transactions:
        op_amount = transaction.get("operationAmount", {})
        currency_code = op_amount.get("currency", {}).get("code")
        if currency_code == currency:
            yield transaction


def transaction_descriptions(
    transactions: List[Dict[str, Any]]
) -> Generator[str, None, None]:
    """
    Генератор описаний транзакций.

    Args:
        transactions: Список словарей с транзакциями

    Yields:
        Описание транзакции
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """
    Генерирует номера карт в формате XXXX XXXX XXXX XXXX.

    Args:
        start: Начальное значение диапазона (включительно)
        stop: Конечное значение диапазона (включительно)

    Yields:
        Отформатированный номер карты
    """
    for number in range(start, stop + 1):
        card_str = str(number).zfill(16)
        formatted = " ".join(card_str[i:i+4] for i in range(0, 16, 4))
        yield formatted
