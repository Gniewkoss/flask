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
