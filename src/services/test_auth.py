# src/services/test_auth.py
import pytest
from unittest.mock import MagicMock
from src.models.user import User
from src.services.auth_service import AuthService, PasswordStrengthValidator

def test_login_success_with_mock():
    mock_repo = MagicMock()
    mock_repo.get_user_by_username.return_value = User(id=1, username="admin", password="123")
    service = AuthService(user_repository=mock_repo)
    assert service.login("admin", "123") is True

def test_login_fail_wrong_password():
    mock_repo = MagicMock()
    mock_repo.get_user_by_username.return_value = User(id=1, username="admin", password="123")
    service = AuthService(user_repository=mock_repo)
    assert service.login("admin", "wrong") is False

def test_login_user_not_found():
    mock_repo = MagicMock()
    mock_repo.get_user_by_username.return_value = None
    service = AuthService(user_repository=mock_repo)
    assert service.login("admin", "123") is False

def test_user_validation_chain():
    fake_chain = PasswordStrengthValidator()
    service = AuthService(user_repository=MagicMock(), validation_chain=fake_chain)
    user = User(id=1, username="admin", password="123")
    service.user_repository.get_user_by_username.return_value = user
    assert service.login("admin", "123") is True
