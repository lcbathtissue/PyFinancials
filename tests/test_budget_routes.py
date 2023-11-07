import unittest
from flask import Flask
from routes.budget_routes import budget_routes

class TestBudgetRoutes(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(budget_routes)
        self.client = self.app.test_client()

    def test_get_budget(self):
        response = self.client.get('/budget')
        self.assertEqual(response.status_code, 200)

    def test_set_budget(self):
        data = {
            'income': 5000,
            'categories': {'Food': 1000, 'Rent': 1500}
        }
        response = self.client.post('/budget', json=data)
        self.assertEqual(response.status_code, 200)

    def test_update_budget(self):
        data = {
            'income': 6000,
            'categories': {'Food': 1200, 'Rent': 1600}
        }
        response = self.client.put('/budget', json=data)
        self.assertEqual(response.status_code, 200)

    def test_get_categories(self):
        response = self.client.get('/budget/categories')
        self.assertEqual(response.status_code, 200)

    def test_delete_budget(self):
        response = self.client.delete('/budget')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
