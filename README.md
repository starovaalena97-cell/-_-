## Модуль generators

Модуль содержит генераторы для эффективной обработки больших объемов транзакций.

### filter_by_currency(transactions, currency)

Фильтрует транзакции по валюте. Возвращает **итератор**.

```python
from src.generators import filter_by_currency

usd_transactions = filter_by_currency(transactions, "USD")
first_usd = next(usd_transactions)