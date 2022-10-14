from flask_login import current_user
from werkzeug.security import check_password_hash

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