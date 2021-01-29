from flask import Flask, jsonify , request

app = Flask(__name__)

items = [
    {
        'name': 'mobile',
        'price':'20000'
    },
    {
        'name': 'dress',
        'price':'2500'
    }
]
@app.route('/items')
def hello():
    return jsonify(items)

@app.route('/<string:name>')
def get_store_name(name):
    for store in items:
        if(store['name'] == name):
            return jsonify(store)
    return jsonify({'message': 'Item is not available in this shop'})

@app.route('/items', methods=['POST'])
def add_movie():
    item = request.get_json()
    items.append(item)
    return {'id': len(items)-1}, 200

app.run()