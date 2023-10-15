"""
A simple Flask application for managing a catalog of people.

This application allows you to add, retrieve, and delete people from a catalog.
"""
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

def load_info():
    '''Load the catalog data from 'catalog.json'.'''
    with open('catalog.json', 'r') as file:
        catalog: list = json.load(file)
    return catalog

def save_info(catalog):
    '''Save the catalog data to 'catalog.json'.'''
    with open('catalog.json', 'w') as file:
        json.dump(catalog, file, indent=4)

@app.route('/get', methods=['GET'])
def get_all():
    '''Retrieve and return the entire catalog.'''
    catalog = load_info()
    return jsonify(catalog)

@app.route('/add', methods=['POST'])
def add_person():
    '''Add a new person to the catalog.'''
    catalog = load_info()
    data = request.get_json()
    catalog.append(data)
    save_info(catalog)
    return jsonify(message='person is added')

@app.route('/get/<int:index>', methods=['GET'])
def get_person(index):
    '''Retrieve and return a specific person from the catalog by their index.'''
    catalog = load_info()
    if index < len(catalog):
        return jsonify(catalog[index])
    else:
        return jsonify(message='invalid index')

@app.route('/delete/<int:index>', methods=['DELETE'])
def delete_person(index):
    '''Delete a person from the catalog by their index.'''
    catalog = load_info()
    if index < len(catalog):
        delete = catalog.pop(index)
        save_info(catalog)
        return jsonify(message=f'Person is deleted {delete}')
    else:
        return jsonify(message='invalid index')

if __name__ == '__main__':
    app.run(debug=True)
