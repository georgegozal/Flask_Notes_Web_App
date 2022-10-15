from flask_login import current_user


APP_URLS = [
    '/login',
    '/sign-up'
]


def test_urls(client):
    for url in APP_URLS:
        response = client.get(url)
        assert response.status_code == 200


def test_redirect(client):
    response = client.get('/', follow_redirects=True)
    assert response.request.path == '/login'


def test_login(client):
    assert client.get('/login').status_code == 200

    with client:
        client.post('/login',data={'email': 'admin@gmail.com','password': 'admin'})
        assert current_user.is_authenticated


def test_failed_register(client):
    assert client.get('/sign-up').status_code == 200
    response = client.post('/sign-up', 
        data={'username': "pytest", 'first_name': 'test', "email": "test_userEmail0555@mail.com",
                "password1": "password5", "password2": "password7"}, 
                    follow_redirects=True)
    assert b'Passwords don`t match.' in response.data


def test_successful_register(client):
    assert client.get('/sign-up').status_code == 200
    response = client.post('/sign-up', 
        data={'username': "pytest", 'first_name': 'test', "email": "test_userEmail0555@mail.com",
                "password1": "password5", "password2": "password5"}, 
                    follow_redirects=True)
    assert response.request.path == '/login'
