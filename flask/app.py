from flask import Flask, request

app = Flask(__name__)

stores = [{"name": "My Store", "items": [{"name": "Chair", "price": 175.50}]}]


# http://127.0.0.1:5000/store
@app.get("/store")
def get_stores():
    return {"stores": stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data.get("name"), "items": []}
    stores.append(new_store)
    return new_store, 201


# http://127.0.0.1:5000/store/My Store/table
@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store.get("name") == name:
            new_item = {"name": request_data.get("name"), "price": request_data.get("price")}
            store["item"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store.get("name") == name:
            return store
    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>/item")
def get_item(name):
    for store in stores:
        if store.get("name") == name:
            return {"items": store.get("items")}
    return {"message": "Store not found"}, 404
