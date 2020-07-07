import sqlite3
from flask_restful import Resource, reqparse

class User():
    TABLE = 'users'

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect("sample.db")
        cursor = connection.cursor()

        username_query = "SELECT * FROM {table} where username = ?".format(table=cls.TABLE)
        result = cursor.execute(username_query, (username,))
        row = result.fetchone()

        if row:
            print(row)
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, id):
        connection = sqlite3.connect("sample.db")
        cursor = connection.cursor()

        username_query = "SELECT * FROM {table} where id = ?".format(table=cls.TABLE)
        result = cursor.execute(username_query, (id,))
        row = result.fetchone()

        if row:
            print(row)
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user



class UserRegister(Resource):
    TABLE = 'users'

    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="username is required"
    )

    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="password is required"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        # insert into db the new user credentials

        connection = sqlite3.connect("sample.db")
        cursor = connection.cursor()

        insert_user = "INSERT INTO {table} VALUES (NULL, ?, ?)".format(table=UserRegister.TABLE)
        try:
            cursor.execute(insert_user, (data['username'], data['password']))
            connection.commit()
            connection.close()
        except Exception as e:
            return {'status': 'User registration failed'}

        return {'status': 'User registration succeeded'}
