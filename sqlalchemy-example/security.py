from werkzeug.security import safe_str_cmp
from models.user import User

def authenticate(username, password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

    return None

def identity(payload):
    return User.find_by_id(payload['identity'])
