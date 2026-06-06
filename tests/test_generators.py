"""
Тесты для модуля generators.
"""

import pytest
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)


@pytest.fixture
def sample_transactions():
    """Фикстура с тестовыми транзакциями для генераторов."""
    return [
        {
            "id": 1,
            "description": "Перевод другу",
            "operationAmount": {
                "amount": "100",
                "currency": {"code": "USD"}
            },
        },
        {
            "id": 2,
            "description": "Покупка продуктов",
            "operationAmount": {
                "amount": "2500",
                "currency": {"code": "RUB"}
            },
        },
        {
            "id": 3,
            "description": "Оплата подписки",
            "operationAmount": {
                "amount": "15.99",
                "currency": {"code": "USD"}
            },
        },
        {
            "id": 4,
            "description": "Кофе с собой",
            "operationAmount": {
                "amount": "350",
                "currency": {"code": "RUB"}
            },
        },
    ]


def test_filter_by_currency_returns_iterator(sample_transactions):
    """Проверяет, что функция возвращает итератор."""
    result = filter_by_currency(sample_transactions, "USD")
    assert hasattr(result, "__iter__")
    assert hasattr(result, "__next__")


def test_filter_by_currency_filters_correctly(sample_transactions):
    """Проверяет фильтрацию по валюте."""
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 2
    for trans in result:
        assert trans["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_no_matches(sample_transactions):
    """Проверяет случай, когда нет транзакций в нужной валюте."""
    result = list(filter_by_currency(sample_transactions, "EUR"))
    assert result == []


def test_filter_by_currency_empty_list():
    """Проверяет обработку пустого списка."""
    result = list(filter_by_currency([], "USD"))
    assert result == []


@pytest.mark.parametrize("curr,exp", [
    ("USD", 2),
    ("RUB", 2),
    ("EUR", 0),
])
def test_filter_by_currency_parametrized(sample_transactions, curr, exp):
    """Параметризованный тест фильтрации."""
    result = list(filter_by_currency(sample_transactions, curr))
    assert len(result) == exp


def test_transaction_descriptions_returns_generator(sample_transactions):
    """Проверяет, что функция возвращает генератор."""
    result = transaction_descriptions(sample_transactions)
    assert hasattr(result, "__iter__")
    assert hasattr(result, "__next__")


def test_transaction_descriptions_yields_correct_values(sample_transactions):
    """Проверяет, что генератор возвращает правильные описания."""
    gen = transaction_descriptions(sample_transactions)
    assert next(gen) == "Перевод другу"
    assert next(gen) == "Покупка продуктов"
    assert next(gen) == "Оплата подписки"
    assert next(gen) == "Кофе с собой"


def test_transaction_descriptions_empty_list():
    """Проверяет обработку пустого списка."""
    gen = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(gen)


def test_transaction_descriptions_missing_description():
    """Проверяет случай, когда у транзакции нет поля description."""
    transactions = [{"id": 1}, {"id": 2, "description": "Есть описание"}]
    gen = transaction_descriptions(transactions)
    assert next(gen) == ""
    assert next(gen) == "Есть описание"


def test_card_number_generator_returns_generator():
    """Проверяет, что функция возвращает генератор."""
    result = card_number_generator(1, 5)
    assert hasattr(result, "__iter__")
    assert hasattr(result, "__next__")


def test_card_number_generator_single_number():
    """Проверяет генерацию одного номера карты."""
    gen = card_number_generator(1, 1)
    assert next(gen) == "0000 0000 0000 0001"


def test_card_number_generator_range():
    """Проверяет генерацию диапазона номеров."""
    result = list(card_number_generator(10, 12))
    expected = [
        "0000 0000 0000 0010",
        "0000 0000 0000 0011",
        "0000 0000 0000 0012",
    ]
    assert result == expected


@pytest.mark.parametrize("start,stop,first,last", [
    (1, 3, "0000 0000 0000 0001", "0000 0000 0000 0003"),
    (100, 101, "0000 0000 0000 0100", "0000 0000 0000 0101"),
    (9999, 10000, "0000 0000 0000 9999", "0000 0000 0001 0000"),
])
def test_card_number_generator_parametrized(start, stop, first, last):
    """Параметризованный тест генератора карт."""
    result = list(card_number_generator(start, stop))
    assert result[0] == first
    assert result[-1] == last


def test_card_number_generator_max():
    """Проверяет максимальное значение."""
    gen = card_number_generator(9999999999999999, 9999999999999999)
    assert next(gen) == "9999 9999 9999 9999"
