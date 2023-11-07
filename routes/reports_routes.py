from flask import Blueprint, request, jsonify
# from PyFinancials import app
from data import income_data, expenses_data

reports_routes = Blueprint('reports_routes', __name__)

# Endpoint to generate income reports
@reports_routes.route('/reports/income', methods=['GET'])
def get_income_reports():
    return jsonify(income_data)

# Endpoint to generate expense reports
@reports_routes.route('/reports/expenses', methods=['GET'])
def get_expense_reports():
    return jsonify(expenses_data)

# Endpoint to calculate and retrieve savings reports
@reports_routes.route('/reports/savings', methods=['GET'])
def get_savings_reports():
    savings_data = {}
    for month, income in income_data.items():
        if month in expenses_data:
            total_expenses = sum(expenses_data[month].values())
            savings = income - total_expenses
            savings_data[month] = savings
    return jsonify(savings_data)
