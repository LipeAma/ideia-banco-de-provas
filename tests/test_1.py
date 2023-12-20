from fastapi.testclient import TestClient

from source.app import app


def test_root_deve_retornar_200_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Olá Mundo!'}


def test_post_create_user1(client):
    data = {
        'username': 'nome',
        'email': 'nome@opa.io',
        'age': 69,
        'password': 'atumalaca',
    }
    expected = {'username': 'nome', 'email': 'nome@opa.io'}
    response = client.post('/', json=data)
    assert response.status_code == 201
    assert response.json() == expected


def test_post_create_user2(client):
    data = {
        'username': 'nome',
        'email': 'nome@opa.io',
        'age': 69,
        'password': 'atumalaca',
    }
    expected = {'username': 'nome', 'email': 'nome@opa.io'}
    response = client.post('/users/', json=data)
    assert response.status_code == 201
    assert response.json() == expected


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == 200
    assert response.json() == {
        'users': [
            {
                'username': 'nome',
                'email': 'nome@opa.io',
                'age': 69,
                'password': 'atumalaca',
                'id': 1,
            }
        ]
    }


def test_put_user(client):
    data = {
        'username': 'jota',
        'email': 'jota@opa.io',
        'age': 20,
        'password': 'atumalaca',
    }
    expected = {
        'username': 'jota',
        'email': 'jota@opa.io',
        'age': 20,
        'password': 'atumalaca',
        'id': 1,
    }
    response = client.put('/users/1', json=data)
    assert response.status_code == 200
    assert response.json() == expected


def test_put_user_raise_exeption_index_out_of_range(client):
    data = {
        'username': 'jota',
        'email': 'jota@opa.io',
        'age': 20,
        'password': 'atumalaca',
    }
    response = client.put('/users/10', json=data)
    assert response.status_code == 404
