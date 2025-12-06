# src/repositories/product_repository.py
from src.models.product import Product

class ProductRepository:
    def __init__(self, database):
        self.db = database
        self.db.connect()  # Asegurarnos de cargar los datos

    def get_all(self):
        return self.db.get_products()

    def get_by_id(self, product_id):
        for p in self.get_all():
            if p.get("id") == product_id:
                return p
        return None

    def create(self, product: Product):
        products = self.get_all()
        new_id = len(products) + 1
        new_product = {
            "id": new_id,
            "name": product.name,
            "category_id": product.category_id,
            "price": product.price
        }
        self.db.add_product(new_product)
        return new_product

