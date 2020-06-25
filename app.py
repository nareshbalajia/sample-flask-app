from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identify

app = Flask(__name__)
app.secret_key = 'flasksample'
api = Api(app)

jwt = JWT(app, authenticate, identify)

items = []

class Item(Resource):

    @jwt_required()
    def get(self, name):
        return next(filter(lambda x: x['name'] == name , items), None), 200

    @jwt_required()
    def post(self, name):
        req_body = request.get_json(silent=True)
        print(req_body)
        items.append({'name': name, 'price': req_body['price']})
        return {'status': 'Item added Successful'}, 200

class ItemList(Resource):
    @jwt_required()
    def get(self):
        print("entering")
        return {'items': items}

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

app.run(port=5000, debug=True)
