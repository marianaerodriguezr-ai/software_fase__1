# src/repositories/in_memory/category_repository.py
from src.models.category import Category

class CategoryRepository:
    def __init__(self):
        self.categories = []
        self._next_id = 1

    def get_all(self):
        return self.categories

    def get_by_name(self, name):
        for c in self.categories:
            if c.name == name:
                return c
        return None

    def create(self, name):
        category = Category(id=self._next_id, name=name)
        self._next_id += 1
        self.categories.append(category)
        return category
