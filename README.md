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

## 📁 Работа с CSV и Excel

Добавлена поддержка загрузки финансовых транзакций из CSV- и Excel-файлов.  
Теперь ты можешь читать данные из разных источников.

### 📄 Модуль `file_reader`

Модуль `src/file_reader.py` предоставляет две функции:

#### `read_csv_transactions(file_path: str) -> List[Dict]`  
Читает CSV-файл с разделителем `;` и возвращает список словарей с транзакциями.

#### `read_excel_transactions(file_path: str) -> List[Dict]`  
Читает Excel-файл (`.xlsx`) и возвращает список словарей с транзакциями.

### 🧪 Пример использования:

```python
from src.file_reader import read_csv_transactions, read_excel_transactions

# Чтение из CSV
transactions_csv = read_csv_transactions('data/transactions.csv')

# Чтение из Excel
transactions_excel = read_excel_transactions('data/transactions_excel.xlsx')

print(f"CSV: {len(transactions_csv)} записей")
print(f"Excel: {len(transactions_excel)} записей")