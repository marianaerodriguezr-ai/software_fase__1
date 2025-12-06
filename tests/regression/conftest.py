# tests/regression/conftest.py
import pytest
from src.services.category_service import CategoryService
from src.services.product_service import ProductService

@pytest.fixture
def category_service():
    return CategoryService()

@pytest.fixture
def product_service():
    return ProductService()
