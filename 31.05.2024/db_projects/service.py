import utils
from typing import Union
from db import commit
from db import cur, conn
from dto import UserRegisterDTO
from models import User, UserRole, UserStatus, TodoType
from sessions import Session
from utils import login_required

from validators import check_validators

session = Session()


@commit
def login(username: str, password: str) -> Union[utils.BadRequest, utils.ResponseData]:
    user: User | None = session.check_session()
    if user:
        return utils.BadRequest('You already logged in', status_code=401)

    get_user_by_username = '''select * from users where username = %s;'''
    cur.execute(get_user_by_username, (username,))
    user_data = cur.fetchone()
    if not user_data:
        return utils.BadRequest('Bad credentials', status_code=401)
    user = User.from_tuple(user_data)
    if user.login_try_count >= 3:
        return utils.BadRequest('User is blocked')
    if not utils.check_password(password, user.password):
        update_count_query = """update users set login_try_count = login_try_count + 1 where username = %s;"""
        cur.execute(update_count_query, (user.username,))
        return utils.BadRequest('Bad credentials', status_code=401)

    session.add_session(user)
    return utils.ResponseData('User Successfully Logged in')


@commit
def register(dto: UserRegisterDTO):
    try:
        check_validators(dto)
        user_data = '''select * from users where username = %s;'''
        cur.execute(user_data, (dto.username,))
        user = cur.fetchone()
        if user:
            return utils.BadRequest('User already registered', status_code=401)

        insert_user_query = """
        insert into users(username,password,role,status,login_try_count)
        values (%s,%s,%s,%s,%s);
        """
        user_data = (dto.username, utils.hash_password(dto.password), UserRole.USER.value, UserStatus.ACTIVE.value, 0)
        cur.execute(insert_user_query, user_data)
        return utils.ResponseData('User Successfully Registered👌')

    except AssertionError as e:
        return utils.BadRequest(e)


def logout():
    global session
    if session.check_session():
        session.session = None
        return utils.ResponseData('User Successfully Logged Out !!!')


@login_required
@commit
def todo_add(title: str):
    insert_query = """insert into todos(name,todo_type,user_id)
        values (%s,%s,%s);
        """
    data = (title, TodoType.Personal.value, session.session.id)

    cur.execute(insert_query, data)
    return utils.ResponseData('INSERTED TODO')


@commit
@login_required
def delete_todo(todo_id: int) -> Union[utils.BadRequest, utils.ResponseData]:
    delete_query = "DELETE FROM todos WHERE id = %s AND user_id = %s;"
    cur.execute(delete_query, (todo_id, session.session.id))
    if cur.rowcount == 0:
        return utils.BadRequest('Todo not found', status_code=404)
    return utils.ResponseData('Todo Successfully Deleted')


@commit
@login_required
def update_todo(todo_id: int, title: str, todo_type: TodoType) -> Union[utils.BadRequest, utils.ResponseData]:
    update_query = """
    UPDATE todos 
    SET name = %s, todo_type = %s 
    WHERE id = %s AND user_id = %s;
    """
    cur.execute(update_query, (title, todo_type.value, todo_id, session.session.id))
    if cur.rowcount == 0:
        return utils.BadRequest('Todo not found', status_code=404)
    return utils.ResponseData('Todo Successfully Updated')


@commit
def block_user(username: str) -> Union[utils.BadRequest, utils.ResponseData]:
    user_data = '''select * from users where username = %s;'''
    cur.execute(user_data, (username,))
    user = cur.fetchone()
    if not user:
        return utils.BadRequest('User not found', status_code=404)

    update_status_query = """update users set status = %s where username = %s;"""
    cur.execute(update_status_query, (UserStatus.BLOCKED.value, username))
    return utils.ResponseData('User Successfully Blocked')