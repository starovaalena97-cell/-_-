"""
Модуль для работы с файлами JSON.
Содержит функции для чтения данных о транзакциях.
"""

import json
import os
from typing import List, Dict, Any


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей с данными транзакций.

    Args:
        file_path: Путь к JSON-файлу

    Returns:
        Список словарей с данными транзакций.
        Если файл не найден, пустой или содержит не список - возвращает пустой список.

    Examples:
        >>> transactions = read_json_file('data/operations.json')
        >>> print(len(transactions))
        5
    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if isinstance(data, list):
            return data
        else:
            return []

    except (json.JSONDecodeError, OSError):
        return []
    