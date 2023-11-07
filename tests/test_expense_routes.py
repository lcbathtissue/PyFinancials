import unittest
from flask import Flask
from routes.expense_routes import expense_routes

class TestExpenseRoutes(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(expense_routes)
        self.client = self.app.test_client()

    def test_get_expenses(self):
        response = self.client.get('/expenses')
        self.assertEqual(response.status_code, 200)

    def test_add_expense(self):
        data = {'amount': 100, 'category': 'Food', 'description': 'Lunch'}
        response = self.client.post('/expenses', json=data)
        self.assertEqual(response.status_code, 200)

    def test_get_expense(self):
        expense_id = 0  # Replace with a valid expense ID
        response = self.client.get(f'/expenses/{expense_id}')
        self.assertEqual(response.status_code, 200)

    def test_update_expense(self):
        expense_id = 0  # Replace with a valid expense ID
        data = {'amount': 150, 'category': 'Food', 'description': 'Dinner'}
        response = self.client.put(f'/expenses/{expense_id}', json=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_expense(self):
        expense_id = 0  # Replace with a valid expense ID
        response = self.client.delete(f'/expenses/{expense_id}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
