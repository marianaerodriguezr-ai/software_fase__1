import pytest
from src.models.category import Category
from src.services.category_service import CategoryService

def test_create_category_success(category_service):
    new_category = category_service.create_category("Ropa")
    assert new_category.id is not None
    assert new_category.name == "Ropa"

def test_create_category_duplicate(category_service):
    category_service.create_category("Ropa")
    with pytest.raises(ValueError):
        category_service.create_category("Ropa")

def test_list_categories(category_service):
    category_service.create_category("Ropa")
    category_service.create_category("Electrónica")
    categories = category_service.list_categories()
    assert len(categories) == 2
    assert categories[0].name == "Ropa"
    assert categories[1].name == "Electrónica"
