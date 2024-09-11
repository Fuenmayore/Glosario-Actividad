from controller.user_controller import UserController
from model.user import UserRepository

def main():
    user_repository = UserRepository()
    user_controller = UserController(user_repository)

    user_id = int(input("Enter user ID: "))
    user_name = user_controller.get_user_name(user_id)

    print(f'User Name: {user_name}')

if __name__ == '__main__':
    main()
