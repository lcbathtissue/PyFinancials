from flask import Blueprint, request, jsonify
# from PyFinancials import app
from data import expenses


expense_routes = Blueprint('expense_routes', __name__)

# Endpoint to retrieve all expenses
@expense_routes.route('/expenses', methods=['GET'])
def get_expenses():
    return jsonify(expenses)

# Endpoint to add a new expense
@expense_routes.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    expenses.append(data)
    return jsonify({'message': 'Expense added successfully'})

# Endpoint to retrieve a specific expense by ID
@expense_routes.route('/expenses/<int:expense_id>', methods=['GET'])
def get_expense(expense_id):
    if expense_id < len(expenses):
        return jsonify(expenses[expense_id])
    return jsonify({'error': 'Expense not found'}), 404

# Endpoint to update an existing expense by ID
@expense_routes.route('/expenses/<int:expense_id>', methods=['PUT'])
def update_expense(expense_id):
    if expense_id < len(expenses):
        data = request.get_json()
        expenses[expense_id] = data
        return jsonify({'message': 'Expense updated successfully'})
    return jsonify({'error': 'Expense not found'}), 404

# Endpoint to delete an expense by ID
@expense_routes.route('/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    if expense_id < len(expenses):
        expenses.pop(expense_id)
        return jsonify({'message': 'Expense deleted successfully'})
    return jsonify({'error': 'Expense not found'}), 404