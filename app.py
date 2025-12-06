# app.py
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))



import json
import os
from flask import Flask
from flask_restful import Api

DB_PATH = "db.json"

# ----------------------------------------------------------------------
# Funciones auxiliares de base de datos
# ----------------------------------------------------------------------
def load_db():
    if not os.path.exists(DB_PATH):
        initial_data = {"categories": [], "products": []}
        with open(DB_PATH, "w") as f:
            json.dump(initial_data, f, indent=4)

    with open(DB_PATH, "r") as f:
        return json.load(f)


def save_db(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=4)


# ----------------------------------------------------------------------
# Lógica de negocio usada por los tests de integración
# ----------------------------------------------------------------------
def create_category(name):
    db = load_db()
    new_id = len(db["categories"]) + 1

    category = {"id": new_id, "name": name}
    db["categories"].append(category)
    save_db(db)
    return category


def list_categories():
    db = load_db()
    return db["categories"]


def create_product(name, price, category_id):
    db = load_db()

    if not any(c["id"] == category_id for c in db["categories"]):
        raise ValueError(f"La categoría {category_id} no existe")

    new_id = len(db["products"]) + 1

    product = {
        "id": new_id,
        "name": name,
        "price": price,
        "category_id": category_id
    }
    db["products"].append(product)
    save_db(db)
    return product


def list_products():
    db = load_db()
    return db["products"]


# ----------------------------------------------------------------------
# create_app() para permitir pruebas de Flask
# ----------------------------------------------------------------------
def create_app():
    app = Flask(__name__)
    api = Api(app)

    # Importar aquí para evitar import circular
    from endpoints.products import ProductsResource
    from endpoints.auth import AuthenticationResource
    from endpoints.categories import CategoriesResource
    from endpoints.favorites import FavoritesResource

    api.add_resource(AuthenticationResource, "/auth")
    api.add_resource(ProductsResource, "/products", "/products/<int:product_id>")
    api.add_resource(CategoriesResource, "/categories", "/categories/<int:category_id>")
    api.add_resource(FavoritesResource, "/favorites")

    return app


# ----------------------------------------------------------------------
# Ejecución normal
# ----------------------------------------------------------------------
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
