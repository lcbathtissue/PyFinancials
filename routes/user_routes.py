from flask import Blueprint, request, jsonify
# from PyFinancials import app
from data import users, user_id_counter

user_routes = Blueprint('user_routes', __name__)

# Endpoint to create a new user profile
@user_routes.route('/users', methods=['POST'])
def create_user():
    global user_id_counter
    global users
    data = request.get_json()
    user_id = user_id_counter
    user_id_counter += 1
    users[user_id] = data
    return jsonify({'user_id': user_id, 'message': 'User profile created successfully'})

# Endpoint to retrieve user details by their unique ID
@user_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id])
    return jsonify({'error': 'User not found'}), 404

# Endpoint to update user information
@user_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        data = request.get_json()
        users[user_id] = data
        return jsonify({'message': 'User information updated successfully'})
    return jsonify({'error': 'User not found'}), 404

# Endpoint to delete a user's profile
@user_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({'message': 'User profile deleted successfully'})
    return jsonify({'error': 'User not found'}), 404