import pytest
from flask import Flask
from flask_restful import Api
from endpoints.categories import CategoriesResource
from endpoints.products import ProductsResource

@pytest.fixture
def app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(CategoriesResource, "/categories")
    api.add_resource(ProductsResource, "/products", "/products/<int:product_id>")
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_category_endpoint(client):
    response = client.post("/categories", json={"name": "Ropa"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Ropa"

def test_list_categories_endpoint(client):
    client.post("/categories", json={"name": "Ropa"})
    response = client.get("/categories")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]["name"] == "Ropa"

def test_create_product_endpoint(client):
    # Crear categoría primero
    cat = client.post("/categories", json={"name": "Electrónica"}).get_json()
    response = client.post("/products", json={
        "name": "Laptop",
        "price": 1500,
        "category_id": cat["id"]
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Laptop"
    assert data["price"] == 1500

def test_list_products_endpoint(client):
    cat = client.post("/categories", json={"name": "Ropa"}).get_json()
    client.post("/products", json={"name": "Camiseta", "price": 100, "category_id": cat["id"]})
    client.post("/products", json={"name": "Pantalón", "price": 200, "category_id": cat["id"]})
    response = client.get("/products")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2

