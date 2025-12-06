import pytest

def test_regression_list_products(product_service, category_service):
    """
    Verifica que se puedan listar todos los productos.
    """
    cat = category_service.create_category("Ropa")
    product_service.create_product("Camiseta", 100, cat.id)
    product_service.create_product("Pantalón", 200, cat.id)
    products = product_service.list_products()
    assert len(products) == 2
    assert products[0].name == "Camiseta"
    assert products[1].name == "Pantalón"

def test_regression_create_product(product_service, category_service):
    """
    Verifica que crear un producto sigue funcionando correctamente.
    """
    cat = category_service.create_category("Electrónica")
    new_product = product_service.create_product("Laptop", 1500, cat.id)
    assert new_product.id is not None
    assert new_product.name == "Laptop"
    assert new_product.price == 1500
