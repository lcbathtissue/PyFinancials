# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///PyFinancials_DB.db'  # Replace with your database URI
# db = SQLAlchemy(app)
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#
# class Expense(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     amount = db.Column(db.Float, nullable=False)
#     category = db.Column(db.String(50), nullable=False)
#     description = db.Column(db.String(200))
#
# class Budget(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     income = db.Column(db.Float, nullable=False)
#
# class Income(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     date = db.Column(db.String(10), nullable=False)
#     amount = db.Column(db.Float, nullable=False)
#
# class Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), unique=True, nullable=False)
#     is_custom = db.Column(db.Boolean, default=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # Nullable for predefined categories


user_id_counter = 1
users = {}
expenses = []
budget = {
    'income': 0,
    'categories': {}
}
income_data = {
    '2023-01': 5000,
    '2023-02': 6000,
}
expenses_data = {
    '2023-01': {'Rent': 1200, 'Groceries': 300, 'Utilities': 200},
    '2023-02': {'Rent': 1200, 'Groceries': 350, 'Utilities': 220},
}
predefined_categories = [
    'Food',
    'Housing',
    'Transportation',
    'Entertainment',
    'Utilities'
]
custom_categories = {}