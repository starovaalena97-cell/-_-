# Bank Widget

Виджет для отображения банковских операций клиента.

## Установка

```bash
poetry install

## Модуль decorators

Модуль содержит декоратор `log` для логирования выполнения функций.

### log(filename=None)

Декоратор логирует выполнение функции:

- **Успех:** записывает `имя_функции ok`
- **Ошибка:** записывает `имя_функции error: тип_ошибки. Inputs: (args), {kwargs}`

```python
from src.decorators import log

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)  # Запись в mylog.txt: "my_function ok"