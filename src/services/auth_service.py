# src/services/auth_service.py
class ValidationHandler:
    """Chain of Responsibility para validaciones."""
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def validate(self, user):
        if self.next_handler:
            return self.next_handler.validate(user)
        return True

class PasswordStrengthValidator(ValidationHandler):
    """Ejemplo: valida la fuerza de la contraseña."""
    def validate(self, user):
        if len(user.password) < 3:
            return False
        return super().validate(user)

class AuthService:
    """Servicio de autenticación."""
    def __init__(self, user_repository=None, validation_chain=None):
        self.user_repository = user_repository
        self.validation_chain = validation_chain

    def login(self, username, password):
        user = self.user_repository.get_user_by_username(username)
        if not user:
            return False
        if self.validation_chain and not self.validation_chain.validate(user):
            return False
        return user.password == password
