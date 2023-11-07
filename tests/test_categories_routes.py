import unittest
from flask import Flask
from routes.categories_routes import categories_routes

class TestCategoriesRoutes(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(categories_routes)
        self.client = self.app.test_client()

    def test_get_predefined_categories(self):
        response = self.client.get('/categories')
        self.assertEqual(response.status_code, 200)

    def test_create_custom_category(self):
        data = {'name': 'CustomCategory1', 'details': 'Category details'}
        response = self.client.post('/categories', json=data)
        self.assertEqual(response.status_code, 200)

    def test_update_custom_category(self):
        category_name = 'CustomCategory1'
        data = {'name': 'UpdatedCategory', 'details': 'Updated details'}
        response = self.client.put(f'/categories/{category_name}', json=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_custom_category(self):
        category_name = 'CustomCategory1'
        response = self.client.delete(f'/categories/{category_name}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
