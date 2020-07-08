from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.items import Item


class ItemResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="price is required"
    )

    @jwt_required()
    def get(self, name):
        item = Item.find_by_name(name)
        if item:
            return item.json(), 200

        return {'status': 'Item not found on inventory'}, 404

    @jwt_required()
    def post(self, name):
        data = ItemResource.parser.parse_args()

        if Item.find_by_name(name):
            return {'status': 'Item already exists'}, 400

        item = Item(name, data['price'])
        try:
            item.save()
            return item.json(), 200
        except Exception as e:
            return {'status': 'Something went wrong with item creation'}, 500

    @jwt_required()
    def delete(self, name):
        item = Item.find_by_name(name)
        if item:
            item.delete()
            return {'status': 'Item deleted.'}
        return {'status': 'Item not found.'}, 404
