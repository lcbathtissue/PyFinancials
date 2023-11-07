from flask import Blueprint, request, jsonify
# from PyFinancials import app
from data import predefined_categories, custom_categories

categories_routes = Blueprint('categories_routes', __name__)

# Endpoint to retrieve a list of predefined expense categories
@categories_routes.route('/categories', methods=['GET'])
def get_predefined_categories():
    return jsonify(predefined_categories)

# Endpoint to allow users to create custom expense categories
@categories_routes.route('/categories', methods=['POST'])
def create_custom_category():
    data = request.get_json()
    category_name = data.get('name')
    if category_name:
        custom_categories[category_name] = data
        return jsonify({'message': 'Custom category created successfully'})
    return jsonify({'error': 'Category name not provided'}), 400

# Endpoint to update the name or details of a custom category
@categories_routes.route('/categories/<string:category_name>', methods=['PUT'])
def update_custom_category(category_name):
    if category_name in custom_categories:
        data = request.get_json()
        custom_categories[category_name] = data
        return jsonify({'message': 'Custom category updated successfully'})
    return jsonify({'error': 'Custom category not found'}), 404

# Endpoint to remove a custom category
@categories_routes.route('/categories/<string:category_name>', methods=['DELETE'])
def delete_custom_category(category_name):
    if category_name in custom_categories:
        del custom_categories[category_name]
        return jsonify({'message': 'Custom category deleted successfully'})
    return jsonify({'error': 'Custom category not found'}), 404