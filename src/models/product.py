# src/models/product.py
class Product:
    def __init__(self, id=None, name="", category_id=None, price=0):
        self.id = id
        self.name = name
        self.category_id = category_id
        self.price = price
