from user import User


users = [
    User(1, 'abc', '123'),
    User(2, 'xyz', '789')
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    user = username_table.get(username, None)
    if user and user.password == password:
        return user

def identify(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
