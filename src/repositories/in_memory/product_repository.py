# src/repositories/in_memory/product_repository.py
from src.models.product import Product

class ProductRepository:
    def __init__(self):
        self.products = []
        self._next_id = 1

    def get_all(self):
        return self.products

    def get_by_id(self, product_id):
        for p in self.products:
            if p.id == product_id:
                return p
        return None

    def create(self, name, price, category_id):
        product = Product(id=self._next_id, name=name, price=price, category_id=category_id)
        self._next_id += 1
        self.products.append(product)
        return product
