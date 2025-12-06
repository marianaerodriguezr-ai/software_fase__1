import pytest

def test_get_products_no_token(client):
    response = client.get("/products")
    assert response.status_code == 401
    assert response.json["message"] == "Unauthorized: token not found"

def test_post_product(client):
    headers = {"Authorization": "abcd1234"}
    new_product = {"name": "Laptop", "price": 1500, "category": "Electrónica"}
    response = client.post("/products", headers=headers, json=new_product)
    assert response.status_code == 201
    assert response.json["name"] == "Laptop"
    assert response.json["category"] == "Electrónica"
