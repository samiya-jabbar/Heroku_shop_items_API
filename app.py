from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Item
import json

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/shop-item-bag'
}

initialize_db(app)

@app.route('/items')
def get_items():
    items = Item.objects().to_json()
    return Response(items, mimetype="application/json", status=200)

@app.route('/items', methods=['POST'])
def add_item():
    body = request.get_json()
    item = Item(**body).save()
    id = item.id
    return {'id': str(id)}, 200

@app.route('/<string:name>')
def get_item(name):
    if name==name:
        items = Item.objects.get(name=name).to_json()
        return Response(items, mimetype="application/json", status=200)
    if name!=name:
        return jsonify({'message': 'Item is not available in this shop'})

app.run()