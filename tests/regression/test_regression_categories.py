# tests/regression/test_regression_categories.py

import pytest

def test_regression_get_all_categories(category_service):
    """
    Verifica que se puedan listar todas las categorías.
    """
    category_service.create_category("Ropa")
    category_service.create_category("Electrónica")
    categories = category_service.list_categories()
    assert len(categories) == 2
    assert categories[0].name == "Ropa"
    assert categories[1].name == "Electrónica"

def test_regression_create_category(category_service):
    """
    Verifica que crear una categoría sigue funcionando correctamente.
    """
    new_category = category_service.create_category("RegTestCategory")
    assert new_category.id is not None
    assert new_category.name == "RegTestCategory"

