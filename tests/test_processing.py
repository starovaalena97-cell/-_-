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
    ]


def test_filter_by_state_default(sample_transactions):
    """Тестирует фильтрацию со значением по умолчанию 'EXECUTED'."""
    result = filter_by_state(sample_transactions)
    assert len(result) == 2
    assert all(t["state"] == "EXECUTED" for t in result)


def test_filter_by_state_canceled(sample_transactions):
    """Тестирует фильтрацию со значением 'CANCELED'."""
    result = filter_by_state(sample_transactions, "CANCELED")
    assert len(result) == 2
    assert all(t["state"] == "CANCELED" for t in result)


def test_filter_by_state_empty_list():
    """Тестирует фильтрацию пустого списка."""
    result = filter_by_state([], "EXECUTED")
    assert result == []


def test_sort_by_date_default(sample_transactions):
    """Тестирует сортировку по умолчанию (убывание)."""
    result = sort_by_date(sample_transactions)
    dates = [t["date"] for t in result]
    assert dates == [
        "2019-07-03T18:35:29.512364",
        "2018-10-14T08:21:33.419441",
        "2018-09-12T21:27:25.241689",
        "2018-06-30T02:08:58.425572",
    ]


def test_sort_by_date_ascending(sample_transactions):
    """Тестирует сортировку по возрастанию."""
    result = sort_by_date(sample_transactions, reverse=False)
    dates = [t["date"] for t in result]
    assert dates == [
        "2018-06-30T02:08:58.425572",
        "2018-09-12T21:27:25.241689",
        "2018-10-14T08:21:33.419441",
        "2019-07-03T18:35:29.512364",
    ]


def test_sort_by_date_empty_list():
    """Тестирует сортировку пустого списка."""
    result = sort_by_date([])
    assert result == []
