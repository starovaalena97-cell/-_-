"""
Модуль декораторов для логирования выполнения функций.
"""

import os
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования выполнения функции.

    Args:
        filename: Имя файла для записи логов.
                 Если не указан, логи выводятся в консоль.

    Returns:
        Декорированная функция

    Example:
        @log(filename="mylog.txt")
        def my_function(x, y):
            return x + y

        my_function(1, 2)  # Запишет "my_function ok" в mylog.txt
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                _write_log(log_message, filename)
                return result
            except Exception as e:
                error_message = (
                    f"{func.__name__} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )
                _write_log(error_message, filename)
                raise
        return wrapper
    return decorator


def _write_log(message: str, filename: Optional[str] = None) -> None:
    """
    Записывает сообщение в файл или выводит в консоль.

    Args:
        message: Текст сообщения
        filename: Имя файла для записи (если None - вывод в консоль)
    """
    if filename:
        os.makedirs(os.path.dirname(filename) or '.', exist_ok=True)
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(message + '\n')
    else:
        print(message)
