from flask import Flask, request, jsonify
import requests


app = Flask(__name__)

users = []
url = "http://127.0.0.1:5000/users"
data = {"name": "Jan", "lastname": "Kowalski"}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())

def find_user_by_id(user_id):
    for user in users:
        if user['id'] == user_id:
            return user
    return None

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = find_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if 'name' in data and 'lastname' in data:
        user = {
            'id': len(users) + 1,
            'name': data['name'],
            'lastname': data['lastname']
        }
        users.append(user)
        return jsonify({'id': user['id']}), 201
    else:
        return jsonify({'error': 'Invalid request body'}), 400

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    user = find_user_by_id(user_id)
    if user:
        data = request.get_json()
        if 'name' in data:
            user['name'] = data['name']
        if 'lastname' in data:
            user['lastname'] = data['lastname']
        return '', 204
    else:
        return jsonify({'error': 'User not found'}), 400

@app.route('/users/<int:user_id>', methods=['PUT'])
def create_or_update_user(user_id):
    data = request.get_json()
    user = find_user_by_id(user_id)
    if user:
        user['name'] = data['name']
        user['lastname'] = data['lastname']
    else:
        user = {
            'id': user_id,
            'name': data['name'],
            'lastname': data['lastname']
        }
        users.append(user)
    return '', 204

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = find_user_by_id(user_id)
    if user:
        users.remove(user)
        return '', 204
    else:
        return jsonify({'error': 'User not found'}), 400

if __name__ == '__main__':
    app.run(debug=True)
