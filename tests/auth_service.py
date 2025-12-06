# tests/test_auth.py

import pytest
from unittest.mock import MagicMock
from src.services.auth_service import AuthService
from src.models.user import User

def test_login_success_with_mock():
    # Mock del repositorio
    mock_repo = MagicMock()
    mock_repo.get_user_by_username.return_value = User(
        id=1, username="admin", password="123"
    )

    service = AuthService(user_repository=mock_repo)

    result = service.login("admin", "123")

    assert result is True
    mock_repo.get_user_by_username.assert_called_once_with("admin")


def test_login_fail_wrong_password():
    mock_repo = MagicMock()
    mock_repo.get_user_by_username.return_value = User(
        id=1, username="admin", password="123"
    )

    service = AuthService(user_repository=mock_repo)

    result = service.login("admin", "wrong")

    assert result is False


def test_login_user_not_found():
    mock_repo = MagicMock()
    mock_repo.get_user_by_username.return_value = None

    service = AuthService(user_repository=mock_repo)

    result = service.login("ghost", "123")

    assert result is False


# 🔎 ejemplo usando ValidationChain
def test_user_validation_chain(mocker):
    fake_chain = mocker.MagicMock()
    fake_chain.validate.return_value = True

    service = AuthService(
        user_repository=MagicMock(),
        validation_chain=fake_chain
    )

    service.register_user({
        "username": "maria",
        "email": "test@test.com",
        "age": 20
    })

    fake_chain.validate.assert_called_once()
