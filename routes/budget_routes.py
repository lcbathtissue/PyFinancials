from flask import Blueprint, request, jsonify
# from PyFinancials import app
from data import budget

budget_routes = Blueprint('budget_routes', __name__)

# Endpoint to retrieve the user's budget details
@budget_routes.route('/budget', methods=['GET'])
def get_budget():
    return jsonify(budget)

# Endpoint to set up a new budget
@budget_routes.route('/budget', methods=['POST'])
def set_budget():
    data = request.get_json()
    budget['income'] = data.get('income', 0)
    budget['categories'] = data.get('categories', {})
    return jsonify({'message': 'Budget set up successfully'})

# Endpoint to update the budget
@budget_routes.route('/budget', methods=['PUT'])
def update_budget():
    data = request.get_json()
    budget['income'] = data.get('income', budget['income'])
    budget['categories'] = data.get('categories', budget['categories'])
    return jsonify({'message': 'Budget updated successfully'})

# Endpoint to get a list of expense categories
@budget_routes.route('/budget/categories', methods=['GET'])
def get_categories():
    return jsonify(list(budget['categories'].keys()))

# Endpoint to delete the budget
@budget_routes.route('/budget', methods=['DELETE'])
def delete_budget():
    budget['income'] = 0
    budget['categories'] = {}
    return jsonify({'message': 'Budget deleted successfully'})