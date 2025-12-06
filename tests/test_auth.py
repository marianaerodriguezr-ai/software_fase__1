# tests/test_auth.py
from src.repositories.user_repository import UserRepository
from src.services.auth_service import AuthService, PasswordStrengthValidator

def test_login_success():
    repo = UserRepository()
    service = AuthService(user_repository=repo)
    assert service.login("admin", "123") is True

def test_login_fail():
    repo = UserRepository()
    service = AuthService(user_repository=repo)
    assert service.login("admin", "wrong") is False
