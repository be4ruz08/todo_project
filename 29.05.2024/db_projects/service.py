from db import cur, conn
from models import User
from sessions import Session
import utils

session = Session()
login_attempts = {}


def login(username: str, password: str):
    user: Session | None = session.check_session()
    if user:
        return utils.BadRequest('You already logged in', status_code=401)

    if username in login_attempts and login_attempts[username] >= 3:
        return utils.BadRequest('Your account has been blocked', status_code=401)

    get_user_by_username = '''select * from users where username = %s;'''
    cur.execute(get_user_by_username, (username,))
    user_data = cur.fetchone()
    if not user_data:
        return utils.BadRequest('Username not found')
    _user = User(username=user_data[1], password=user_data[2], role=user_data[3], status=user_data[4],
                 login_try_count=user_data[5])

    if password != _user.password:
        login_attempts[username] = login_attempts.get(username, 0) + 1
        if login_attempts[username] >= 3:
            return utils.BadRequest('Your account has been blocked', status_code=401)
        else:
            return utils.BadRequest('Wrong password', status_code=401)

    if username in login_attempts:
        del login_attempts[username]

    user.add_session(_user)
    return utils.ResponseData('User Successfully Logged in')


while True:
    choice = input('Enter your choice: ')
    if choice == '1':
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        login(username, password)
    else:
        break
