# src/services/product_service.py
from src.repositories.in_memory.product_repository import ProductRepository

class ProductService:
    def __init__(self, repository=None):
        self.repository = repository or ProductRepository()

    def list_products(self):
        return self.repository.get_all()

    def create_product(self, name, price, category_id):
        if price <= 0:
            raise ValueError("Price must be positive")
        return self.repository.create(name, price, category_id)

    def get_product_by_id(self, product_id):
        return self.repository.get_by_id(product_id)
