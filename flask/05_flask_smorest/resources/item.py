import uuid
from flask.views import MethodView

# General improvements for our first REST API
from flask_smorest import Blueprint, abort

from schemas import ItemSchema, ItemUpdateSchema
from db import items

blp = Blueprint("Items", "items", description="Operations on items")


# Data model improvements for our API
# How to use Blueprints and MethodViews in Flask
@blp.route("/item/<string:item_id>")
class Item(MethodView):
    # How to perform data validation with mashmallow
    # Decorating responses with Flask-Smorest
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            # General improvements for our first REST API
            abort(404, message="Item not found.")

    # New endpoints for our first REST API
    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, message="Item not found.")

    # New endpoints for our first REST API
    # How to perform data validation with mashmallow
    # Decorating responses with Flask-Smorest
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        try:
            item = items[item_id]

            # https://blog.teclado.com/python-dictionary-merge-update-operators/
            item |= item_data

            return item
        except KeyError:
            abort(404, message="Item not found.")


# How to use Blueprints and MethodViews in Flask
@blp.route("/item")
class ItemList(MethodView):
    # Decorating responses with Flask-Smorest
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return items.values()

    # New endpoints for our first REST API
    # How to perform data validation with mashmallow
    # Decorating responses with Flask-Smorest
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        for item in items.values():
            if item_data["name"] == item["name"] and item_data["store_id"] == item["store_id"]:
                abort(400, message="Item already exists.")

        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item

        return item
