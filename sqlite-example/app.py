from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from items import Items

app = Flask(__name__)
app.secret_key = 'sample'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Items, '/items/<string:name>')
api.add_resource(UserRegister, '/register')



if __name__ == '__main__':
    app.run(debug=True)
