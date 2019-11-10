#!flask/bin/python 
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
stores = [
	{
		'name': 'Store1',
		'items': [
			{
				'name': 'Batman toy',
				'price': 44.76
			}
		],
	},
	{
		'name': 'Store2',
		'items': [
			{
				'name': 'Superman toy',
				'price': 64.76
			}
		]
	}
]

@app.route('/')
def home():
	return render_template('index.html ')

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
	request_data =  request.get_json()
	new_store = {
		'name': request_data['name'],
		'items': []
	}
	stores.append(new_store)
	return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
	for store in stores:
		if store['name'] == name:
			return jsonify(store)
	return jsonify({'message': 'Store not found'})		

# GET /store
@app.route('/store')
def get_stores():
	return jsonify({'stores': stores})

# POST /store/<string:name>/itam {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
	request_data = request.get_json()
	new_item = {
		'name': request_data['name'],
		'price': float(request_data['price'])
	}
	for store in stores:
		if store['name'] == name:
			store['items'].append(new_item)
			return jsonify(new_item)
	return jsonify({'message': 'Store not found'})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
	for store in stores:
		if store['name'] == name:
			return jsonify({'items': store['items']})

	return jsonify({'message': 'Store not found'})

if __name__ == '__main__':
	app.run(port=5000, debug=True)

