import unittest
from flask import Flask
from routes.user_routes import user_routes

class TestUserRoutes(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(user_routes)
        self.client = self.app.test_client()

    def test_create_user(self):
        data = {
            "username": "test_user",
        }
        response = self.client.post('/users', json=data)
        self.assertEqual(response.status_code, 200)

    def test_get_user(self):
        user_id = 1
        response = self.client.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        user_id = 1
        data = {
            "username": "updated_username",
        }
        response = self.client.put(f'/users/{user_id}', json=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        user_id = 1  # Replace with an existing user ID from your data
        response = self.client.delete(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
