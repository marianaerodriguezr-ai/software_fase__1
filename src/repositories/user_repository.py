from src.models.user import User

class UserRepository:
    """Simula un repositorio de usuarios."""
    def __init__(self):
        # Datos simulados
        self.users = [
            User(id=1, username="admin", password="123"),
            User(id=2, username="user", password="abc"),
        ]

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None
