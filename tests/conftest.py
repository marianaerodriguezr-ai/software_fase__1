# tests/conftest.py
import pytest
from app import create_app

@pytest.fixture
def app():
    """Crea una instancia de Flask para pruebas."""
    app = create_app()
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    """Proporciona un cliente de pruebas de Flask."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Proporciona un runner de comandos de Flask."""
    return app.test_cli_runner()
