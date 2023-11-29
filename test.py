import json
import pytest
from main import app, users

@pytest.fixture
def client():
    return app.test_client()

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert json.loads(response.get_data()) == users

def test_get_user(client):
    response = client.get('/users/1')
    assert response.status_code == 200
    assert json.loads(response.get_data()) == {'id': 1, 'name': 'Gniewko', 'lastname': 'Koscielak'}


def test_get_user_not_found(client):
    response = client.get('/users/100')
    assert response.status_code == 404
    assert json.loads(response.get_data()) == {'error': 'User not found'}

def test_create_user(client):
    response = client.post('/users', json={'name': 'Jan', 'lastname': 'Kowalski'})
    assert response.status_code == 201
    assert json.loads(response.get_data()) == {'id': 7}

def test_create_user_invalid_body(client):
    response = client.post('/users', json={'name': 'Jan'})
    assert response.status_code == 400
    assert json.loads(response.get_data()) == {'error': 'Invalid request body'}

def test_update_user(client):
    response = client.patch('/users/1', json={'name': 'Jan', 'lastname': 'Kowalski'})
    assert response.status_code == 204
    assert response.data == b''

def test_update_user_not_found(client):
    response = client.patch('/users/100', json={'name': 'Jan', 'lastname': 'Kowalski'})
    assert response.status_code == 400
    assert json.loads(response.get_data()) == {'error': 'User not found'}

def test_create_or_update_user(client):
    response = client.put('/users/1', json={'name': 'Jan', 'lastname': 'Kowalski'})
    assert response.status_code == 204
    assert response.data == b''

def test_create_or_update_user_not_found(client):
    response = client.put('/users/100', json={'name': 'Jan', 'lastname': 'Kowalski'})
    assert response.status_code == 204
    assert response.data == b''
def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == 204
    assert response.data == b''

def test_delete_user_not_found(client):
    response = client.delete('/users/80')
    assert response.status_code == 400
    assert json.loads(response.get_data()) == {'error': 'User not found'}