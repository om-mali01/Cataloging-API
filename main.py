from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def load_info():
    with open('catalog.json', 'r') as file:
        catalog = json.load(file)
    return catalog

def save_info(catalog):
    with open('catalog.json', 'w') as file:
        json.dump(catalog, file, indent=4)

@app.route('/get', methods=['GET'])
def get_all():
    catalog = load_info()
    return jsonify(catalog)

@app.route('/add', methods=['POST'])
def add_person():
    catalog = load_info()
    data = request.get_json()
    catalog.append(data)
    save_info(catalog)
    return jsonify(message='person is added')

@app.route('/get/<int:index>', methods=['GET'])
def get_person(index):
    catalog = load_info()
    if index < len(catalog):
        return jsonify(catalog[index])
    else:
        return jsonify(message='invalid index')

@app.route('/delete/<int:index>', methods=['DELETE'])
def delete_person(index):
    catalog = load_info()
    if index < len(catalog):
        delete = catalog.pop(index)
        save_info(catalog)
        return jsonify(message=f'Person is deleted {delete}')
    else:
        return jsonify(message='invalid index')

if __name__ == '__main__':
    app.run(debug=True)