from model.user import UserRepository

class UserController:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_user_name(self, user_id):
        user = self.user_repository.find_user_by_id(user_id)
        if user:
            return user.name
        else:
            return 'User not found'
