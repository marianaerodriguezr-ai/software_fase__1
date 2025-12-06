# src/repositories/interfaces/category_repository_interface.py
from abc import ABC, abstractmethod

class ICategoryRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, category):
        pass

    @abstractmethod
    def delete(self, name):
        pass
