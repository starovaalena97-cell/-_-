"""
Модуль для обработки данных транзакций: фильтрация и сортировка.
"""

from typing import List, Dict, Any


def filter_by_state(
    transactions: List[Dict[str, Any]], state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """
    Фильтрует список транзакций по значению ключа 'state'.

    Args:
        transactions: Список словарей с данными о транзакциях
        state: Значение для фильтрации (по умолчанию 'EXECUTED')

    Returns:
        Новый список транзакций с указанным статусом
    """
    result = []
    for transaction in transactions:
        if transaction.get("state") == state:
            result.append(transaction)
    return result


def sort_by_date(
    transactions: List[Dict[str, Any]], reverse: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует список транзакций по дате.

    Args:
        transactions: Список словарей с данными о транзакциях
        reverse: Порядок сортировки (True - убывание, False - возрастание)

    Returns:
        Новый отсортированный список транзакций
    """
    return sorted(
        transactions,
        key=lambda x: x.get("date", ""),
        reverse=reverse,
    )
