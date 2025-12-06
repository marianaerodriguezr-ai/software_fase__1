import pytest
from src.services.product_service import ProductService

def test_create_product_success(product_service, category_service):
    category = category_service.create_category("Ropa")
    product = product_service.create_product("Camiseta", 100, category.id)
    assert product.id is not None
    assert product.name == "Camiseta"
    assert product.price == 100
    assert product.category_id == category.id

def test_create_product_invalid_price(product_service, category_service):
    category = category_service.create_category("Ropa")
    with pytest.raises(ValueError):
        product_service.create_product("Camiseta", -50, category.id)

def test_list_products(product_service, category_service):
    cat1 = category_service.create_category("Ropa")
    cat2 = category_service.create_category("Electrónica")
    product_service.create_product("Camiseta", 100, cat1.id)
    product_service.create_product("Laptop", 1500, cat2.id)
    products = product_service.list_products()
    assert len(products) == 2
    assert products[0].name == "Camiseta"
    assert products[1].name == "Laptop"

def test_get_product_by_id(product_service, category_service):
    category = category_service.create_category("Ropa")
    product = product_service.create_product("Camiseta", 100, category.id)
    found = product_service.get_product_by_id(product.id)
    assert found.id == product.id
    assert found.name == product.name

def test_get_product_not_found(product_service):
    product = product_service.get_product_by_id(999)
    assert product is None
