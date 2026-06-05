"""
Тесты для модуля processing.
"""

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_transactions():
    """Фикстура с тестовыми транзакциями."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 3, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 4, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 5, "state": "PENDING", "date": "2020-01-01T00:00:00"},
    ]


@pytest.fixture
def transactions_same_dates():
    """Фикстура с транзакциями, имеющими одинаковые даты."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-01T00:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
    ]


def test_filter_by_state_executed(sample_transactions):
    """Тест фильтрации по статусу EXECUTED."""
    result = filter_by_state(sample_transactions, "EXECUTED")
    assert len(result) == 2
    assert all(t["state"] == "EXECUTED" for t in result)


def test_filter_by_state_canceled(sample_transactions):
    """Тест фильтрации по статусу CANCELED."""
    result = filter_by_state(sample_transactions, "CANCELED")
    assert len(result) == 2
    assert all(t["state"] == "CANCELED" for t in result)


def test_filter_by_state_pending(sample_transactions):
    """Тест фильтрации по статусу PENDING."""
    result = filter_by_state(sample_transactions, "PENDING")
    assert len(result) == 1
    assert all(t["state"] == "PENDING" for t in result)


def test_filter_by_state_nonexistent(sample_transactions):
    """Тест фильтрации по несуществующему статусу."""
    result = filter_by_state(sample_transactions, "NONEXISTENT")
    assert len(result) == 0


def test_filter_by_state_default(sample_transactions):
    """Тест фильтрации со значением по умолчанию."""
    result = filter_by_state(sample_transactions)
    assert len(result) == 2
    assert all(t["state"] == "EXECUTED" for t in result)


def test_filter_by_state_empty_list():
    """Тест фильтрации пустого списка."""
    result = filter_by_state([], "EXECUTED")
    assert result == []


def test_sort_by_date_default_descending(sample_transactions):
    """Тест сортировки по умолчанию (убывание)."""
    result = sort_by_date(sample_transactions)
    dates = [t["date"] for t in result]
    assert dates == [
        "2020-01-01T00:00:00",
        "2019-07-03T18:35:29.512364",
        "2018-10-14T08:21:33.419441",
        "2018-09-12T21:27:25.241689",
        "2018-06-30T02:08:58.425572",
    ]


def test_sort_by_date_ascending(sample_transactions):
    """Тест сортировки по возрастанию."""
    result = sort_by_date(sample_transactions, reverse=False)
    dates = [t["date"] for t in result]
    assert dates == [
        "2018-06-30T02:08:58.425572",
        "2018-09-12T21:27:25.241689",
        "2018-10-14T08:21:33.419441",
        "2019-07-03T18:35:29.512364",
        "2020-01-01T00:00:00",
    ]


def test_sort_by_date_same_dates(transactions_same_dates):
    """Тест сортировки при одинаковых датах."""
    result = sort_by_date(transactions_same_dates)
    assert len(result) == 3


def test_sort_by_date_empty_list():
    """Тест сортировки пустого списка."""
    result = sort_by_date([])
    assert result == []


def test_sort_by_date_missing_date():
    """Тест сортировки с отсутствующими датами."""
    transactions = [
        {"id": 1, "date": "2024-01-01"},
        {"id": 2},
        {"id": 3, "date": "2023-01-01"},
    ]
    result = sort_by_date(transactions)
    assert result[-1]["id"] == 2
