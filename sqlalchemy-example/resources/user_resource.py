from flask_restful import Resource, reqparse

from models.user import User


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="Username is required"
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="password is required"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {'Status': 'Username already exists'}, 400

        new_user = User(data['username'], data['password'])
        try:
            new_user.save()
            return {'status': 'User registration successful'}, 200
        except Exception as e:
            return {'status': 'Something went wrong with user registration'}, 500
