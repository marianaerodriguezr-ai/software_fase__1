# src/services/category_service.py
from src.repositories.in_memory.category_repository import CategoryRepository

class CategoryService:
    def __init__(self, repository=None):
        self.repository = repository or CategoryRepository()

    def list_categories(self):
        return self.repository.get_all()

    def create_category(self, name):
        if self.repository.get_by_name(name):
            raise ValueError("Category already exists")
        return self.repository.create(name)
