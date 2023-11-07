import unittest
from flask import Flask
from routes.reports_routes import reports_routes

class TestReportsRoutes(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(reports_routes)
        self.client = self.app.test_client()

    def test_get_income_reports(self):
        response = self.client.get('/reports/income')
        self.assertEqual(response.status_code, 200)

    def test_get_expense_reports(self):
        response = self.client.get('/reports/expenses')
        self.assertEqual(response.status_code, 200)

    def test_get_savings_reports(self):
        response = self.client.get('/reports/savings')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
