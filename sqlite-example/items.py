from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

import sqlite3

class Items(Resource):
    TABLE = 'items'

    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="Price required!"
    )

    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item

        return {'status': 'item not found!'}, 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect("sample.db")
        cursor = connection.cursor()

        get_item_query = "SELECT * FROM {table} WHERE name=?".format(table=cls.TABLE)
        result = cursor.execute(get_item_query, (name,))
        row = result.fetchone()
        if row:
            return {'item': {'name': row[0], 'price': row[1]}}
        return None

    @jwt_required()
    def post(self, name):
        data = Items.parser.parse_args()
        try:
            post_status = self.insert(name, data['price'])
            return {'status': 'Item push successful!'}
        except Exception as e:
            print(e)
            return {'status': 'Item push failed!'}

    @classmethod
    def insert(cls, name, price):

        connection = sqlite3.connect("sample.db")
        cursor = connection.cursor()

        insert_query = "INSERT INTO {table} VALUES(?, ?)".format(table=cls.TABLE)

        result = cursor.execute(insert_query, (name, price))
        connection.commit()
        connection.close()
