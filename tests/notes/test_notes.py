from flask_login import current_user


def test_notes(client):
    response = client.get('/', follow_redirects=True)
    assert response.request.path == '/login'

    with client:
        client.post('/login',data={'email': 'admin@gmail.com','password': 'admin'})
        assert current_user.is_authenticated

    assert client.get('/').status_code == 200
    response = client.post('/',
        data={'text': 'Pytest fixtures allow writing pieces of code that are reusable across tests.'})
