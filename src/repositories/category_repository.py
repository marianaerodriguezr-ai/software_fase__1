# src/repositories/category_repository.py
from src.repositories.interfaces.category_repository_interface import ICategoryRepository

class CategoryRepository(ICategoryRepository):
    def __init__(self, database):
        self.db = database

    def get_all(self):
        return self.db.get_categories()

    def create(self, category):
        self.db.add_category(category)
        return category

    def delete(self, name):
        self.db.remove_category(name)
        return True
