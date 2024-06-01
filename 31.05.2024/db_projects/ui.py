from utils import ResponseData, BadRequest
import service
from typing import Union

from colorama import Fore

from dto import UserRegisterDTO


def print_response(response: Union[ResponseData,BadRequest]):
    color = Fore.GREEN if response.status_code == 200 else Fore.RED
    print(color + response.data + Fore.RESET)


def login():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    response = service.login(username, password)
    print_response(response)


def register():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    dto: UserRegisterDTO = UserRegisterDTO(username, password)
    response = service.register(dto)
    print_response(response)


def logout():
    response = service.logout()
    print_response(response)


def todo_add():
    title = input('Enter title : ')
    response = service.todo_add(title)
    print_response(response)


# CRUD =>


def block_user():
    pass


def menu():
    print('1. Login')
    print('2. Register')
    print('3. Logout')
    print('4. Todo Add')
    print('5. Exit ')
    return input('Enter your choice ?: ')


if __name__ == '__main__':
    while True:
        choice = menu()
        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == '3':
            logout()
        elif choice == '4':
            todo_add()
        elif choice == 'q':
            break
