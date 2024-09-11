class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return f'User(id={self.user_id}, name={self.name})'


class UserRepository:
    def __init__(self):
        # base de datos de usuarios
        self.users = [
            User(1, 'John Doe'),
            User(2, 'Jane Smith'),
            User(3, 'Yay Castro'),
            User(4, 'Edwin Fuenmayor'),
            User(5, 'Ibero Americana'),
            User(6, 'Juancho')
        ]

    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
