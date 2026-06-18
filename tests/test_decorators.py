"""
Тесты для модуля decorators.
"""

import os
import tempfile

import pytest

from src.decorators import log


def test_log_to_console_success(capsys):
    """Тест логирования успешного выполнения в консоль."""

    @log()
    def add(a, b):
        return a + b

    result = add(1, 2)
    assert result == 3

    captured = capsys.readouterr()
    assert "add ok" in captured.out


def test_log_to_console_error(capsys):
    """Тест логирования ошибки в консоль."""

    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out


def test_log_to_file_success():
    """Тест логирования успешного выполнения в файл."""
    with tempfile.NamedTemporaryFile(mode="r+", delete=False) as tmp_file:
        tmp_filename = tmp_file.name

    try:

        @log(filename=tmp_filename)
        def multiply(a, b):
            return a * b

        result = multiply(2, 3)
        assert result == 6

        # Проверяем содержимое файла
        with open(tmp_filename, "r", encoding="utf-8") as f:
            content = f.read()
            assert "multiply ok" in content
    finally:
        os.unlink(tmp_filename)


def test_log_to_file_error():
    """Тест логирования ошибки в файл."""
    with tempfile.NamedTemporaryFile(mode="r+", delete=False) as tmp_file:
        tmp_filename = tmp_file.name

    try:

        @log(filename=tmp_filename)
        def divide(a, b):
            return a / b

        with pytest.raises(ZeroDivisionError):
            divide(1, 0)

        # Проверяем содержимое файла
        with open(tmp_filename, "r", encoding="utf-8") as f:
            content = f.read()
            assert "divide error: ZeroDivisionError" in content
            assert "Inputs: (1, 0), {}" in content
    finally:
        os.unlink(tmp_filename)


def test_log_with_multiple_args(capsys):
    """Тест логирования с несколькими аргументами."""

    @log()
    def calculate(a, b, c=0):
        return a + b + c

    result = calculate(1, 2, c=3)
    assert result == 6

    captured = capsys.readouterr()
    assert "calculate ok" in captured.out


def test_log_with_filename_none(capsys):
    """Тест логирования когда filename=None."""

    @log(filename=None)
    def test_func():
        return "test"

    result = test_func()
    assert result == "test"

    captured = capsys.readouterr()
    assert "test_func ok" in captured.out


def test_log_preserves_function_name():
    """Тест что декоратор сохраняет имя функции."""

    @log()
    def my_special_function():
        pass

    assert my_special_function.__name__ == "my_special_function"
