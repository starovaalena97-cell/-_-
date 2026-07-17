"""
Модуль для работы с внешним API конвертации валют.
"""

import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# API ключ из .env
API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
BASE_URL = 'http://api.exchangeratesapi.io/v1/latest'


def get_exchange_rate(from_currency: str, to_currency: str = 'RUB'):
    """
    Получает курс обмена валюты через внешнее API.

    Args:
        from_currency: Код исходной валюты (например, 'USD')
        to_currency: Код целевой валюты (по умолчанию 'RUB')

    Returns:
        Курс обмена или None в случае ошибки
    """
    if not API_KEY:
        return None

    params = {
        'access_key': API_KEY,
        'base': from_currency,
        'symbols': to_currency
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get('success'):
            rates = data.get('rates', {})
            return rates.get(to_currency)
        return None

    except Exception:
        return None


def convert_to_rubles(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction: Словарь с данными транзакции

    Returns:
        Сумма в рублях (float)
    """
    try:
        amount_str = transaction.get('operationAmount', {}).get('amount', '0')
        currency_code = transaction.get('operationAmount', {}).get('currency', {}).get('code', 'RUB')

        amount = float(amount_str)

        if currency_code == 'RUB':
            return amount

        rate = get_exchange_rate(currency_code)

        if rate is None:
            return 0.0

        return round(amount * rate, 2)

    except (ValueError, TypeError, AttributeError):
        return 0.0
