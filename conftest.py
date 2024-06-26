import pytest

from main import BooksCollector

# Фикстура для создания нового экземпляра BooksCollector
@pytest.fixture
def collector():
    return BooksCollector()