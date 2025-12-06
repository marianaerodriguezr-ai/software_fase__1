# src/repositories/interfaces/product_repository_interface.py

from abc import ABC, abstractmethod

class IProductRepository(ABC):
    @abstractmethod
    def get_all(self):
        """Devuelve todos los productos"""
        pass

    @abstractmethod
    def get_by_id(self, product_id):
        """Devuelve un producto por su ID"""
        pass

    @abstractmethod
    def create(self, product):
        """Crea un nuevo producto"""
        pass

    @abstractmethod
    def delete(self, product_id):
        """Elimina un producto por su ID"""
        pass

    @abstractmethod
    def update(self, product_id, new_data):
        """Actualiza un producto existente"""
        pass
